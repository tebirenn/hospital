from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('READ', 'Read'),
        ('ARCHIVED', 'Archived'),
    )
    TYPE_CHOICES = (
        ('VISIT_CREATED', 'Visit created'),
        ('VISIT_CANCELED', 'Visit canceled'),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    type = models.CharField(choices=TYPE_CHOICES, max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'R: {self.recipient.username}, M: {self.message[:25]}'