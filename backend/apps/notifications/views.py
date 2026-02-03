from rest_framework import viewsets, mixins
from .models import Notification
from .serializers import NotificationSerializer

# Only allow listing and updating (to mark as read)
class NotificationViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = NotificationSerializer
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
