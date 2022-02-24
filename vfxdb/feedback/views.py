from api.serializer import FeedBackserializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class FeedBackView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        user=self.request.user
        feedback = FeedBackPost.objects.filter(user=user)
        serializer = FeedBackserializer(feedback, many = True)
        return Response(serializer.data)
