from api.serializer import Signalserializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class SignalView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = Signalserializer

    def get_queryset(self):
        user=self.request.user
        return Signals.objects.filter(manager=user).order_by('-id')[0]
