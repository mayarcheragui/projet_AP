from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    target_date = models.DateField()
    is_completed = models.BooleanField(default=False)
