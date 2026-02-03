from rest_framework import serializers
from .models import Task, Journal

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_done', 'date', 'goal']

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'content', 'created_at']
