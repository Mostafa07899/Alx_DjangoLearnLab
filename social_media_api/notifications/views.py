from django.shortcuts import render
from .models import Notification
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer

# Create your views here.


class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.all()