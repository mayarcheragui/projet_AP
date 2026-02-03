from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.goals.models import Goal
from .models import Notification

@receiver(post_save, sender=Goal)
def notify_goal_events(sender, instance, created, **kwargs):
    # Création d'un nouvel objectif
    if created:
        message = f"Nouvel objectif créé : {instance.title}. Bonne chance !"
        Notification.objects.create(
            user=instance.user,
            message=message,
            is_read=False
        )

    # Objectif marqué comme complété (Update)
    elif instance.is_completed:
        message = f"Félicitations ! Vous avez atteint votre objectif : {instance.title}"
        
        Notification.objects.get_or_create(
            user=instance.user,
            message=message,
            is_read=False
        )
