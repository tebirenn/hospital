from django.db import models
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.FloatField()
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Visit(models.Model):
    STATUS_CHOICES = (
        ('PLANNED', 'Planned'),
        ('COMPLETED', 'Completed'),
        ('CANCELED', 'Canceled'),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    notes = models.TextField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)

    def __str__(self):
        return f'D: {self.schedule.doctor} -- P: {self.patient}'


