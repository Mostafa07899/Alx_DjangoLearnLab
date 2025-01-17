from rest_framework import serializers
from .models import Notification



class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'verb', 'target', 'timastamp']
        read_only_fields = ['id', 'timestamp']
