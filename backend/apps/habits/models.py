from django.db import models
from django.conf import settings
from apps.goals.models import Goal

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

class Journal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
