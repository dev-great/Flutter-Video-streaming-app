from api.serializer import Notificationserializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class NotificationView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        notifications = NotificationPost.objects.all()
        serializer = Notificationserializer(notifications, many = True)
        return Response(serializer.data)
