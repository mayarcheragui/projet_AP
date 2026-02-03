from rest_framework import viewsets, permissions
from .models import Goal
from .serializers import GoalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.habits.models import Task, Journal


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserAnalyticsView(APIView):
    def get(self, request):
        user = request.user
        
        tasks = Task.objects.filter(user=user)
        total_tasks = tasks.count()
        completed_task_ids = list(tasks.filter(is_done=True).values_list('id', flat=True))
        pending_task_ids = list(tasks.filter(is_done=False).values_list('id', flat=True))
        
        goals = Goal.objects.filter(user=user)
        total_goals = goals.count()
        completed_goal_ids = list(goals.filter(is_completed=True).values_list('id', flat=True))
        active_goal_ids = list(goals.filter(is_completed=False).values_list('id', flat=True))
        
        journal_ids = list(Journal.objects.filter(user=user).values_list('id', flat=True))

        # taux global
        completion_rate = (len(completed_task_ids) / total_tasks * 100) if total_tasks > 0 else 0

        return Response({
            "summary": {
                "user": user.username,
                "completion_rate": f"{round(completion_rate, 1)}%"
            },
            "tasks": {
                "total_count": total_tasks,
                "completed": {
                    "count": len(completed_task_ids),
                    "ids": completed_task_ids
                },
                "pending": {
                    "count": len(pending_task_ids),
                    "ids": pending_task_ids
                }
            },
            "goals": {
                "total_count": total_goals,
                "completed": {
                    "count": len(completed_goal_ids),
                    "ids": completed_goal_ids
                },
                "active": {
                    "count": len(active_goal_ids),
                    "ids": active_goal_ids
                }
            },
            "journal": {
                "total_entries": len(journal_ids),
                "entry_ids": journal_ids
            }
        })
