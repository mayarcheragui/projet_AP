from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Goal
        fields = ['id', 'title', 'target_date', 'is_completed', 'tasks']
