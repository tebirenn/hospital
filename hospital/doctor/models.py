from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=255)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'