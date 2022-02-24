
import pyotp
import base64
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from .models import OTPVerification
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from api.serializer import Userserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    @staticmethod
    def get(request, phone):
        try:
            phonenumber = OTPVerification.objects.get(phonenumber=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            OTPVerification.objects.create(
                phonenumber=phone,
            )
            phonenumber = OTPVerification.objects.get(phonenumber=phone)  # user Newly created Model
        phonenumber.counter += 1  # Update Counter At every Call
        phonenumber.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(phonenumber.counter))
        msg = f'DO NOT DISCLOSE. Dear Customer, The OTP for your confirmation is : {OTP.at(phonenumber.counter)} to verify {phonenumber}. Thank you for choosing VFX.'
        send_mail('VFX OTP Verification', msg, settings.EMAIL_HOST_USER,
        [settings.RECIPIENT_ADDRESS], fail_silently=False)
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(phonenumber.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            phonenumber = OTPVerification.objects.get(phonenumber=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  
        
                # HOTP Model
        if OTP.verify(request.data["otp"], phonenumber.counter):  # Verifying the OTP
            phonenumber.isVerified = True
            phonenumber.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)



class RegisterView(APIView):
    @csrf_protect
    def post(self, request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})

class FacebookLogin(SocialLoginView):
    
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter