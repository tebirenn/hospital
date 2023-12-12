from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Service, Schedule, Visit
from notifications.models import Notification

@receiver(post_save, sender=Service)
def post_save_service(created, **kwargs):
    if created:
        print('Сервис был создан!')
    else:
        print('Сервис был обновлен!')

@receiver(pre_save, sender=Schedule)
def pre_save_schedule(instance, **kwargs):
    instance.end = instance.start + timezone.timedelta(hours=1)

@receiver(post_save, sender=Visit)
def post_save_visit(instance, created, **kwargs):
    if created:
        user = User.objects.get(pk=1)
        Notification.objects.create(
            recipient=user,
            message=f'Visit: {instance}, was created!',
            status='NEW',
            type='VISIT_CREATED',
        )