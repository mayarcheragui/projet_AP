from rest_framework import viewsets, permissions
from .models import Task, Journal
from .serializers import TaskSerializer, JournalSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        task = serializer.save()

        # Si la tâche appartient à un objectif
        if task.goal:
            goal = task.goal
            all_tasks_done = goal.tasks.filter(is_done=False).count() == 0
            
            if all_tasks_done:
                goal.is_completed = True
                goal.save() 


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
