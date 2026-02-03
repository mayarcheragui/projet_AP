from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'created_at']
        # Notifications are usually read-only, except for marking them as 'is_read'
        read_only_fields = ['id', 'message', 'created_at']
