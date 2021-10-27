from django.db import models
from core.models import Superstructure


class Schedule(models.Model):
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    description = models.TextChoices('Event', 'Rent Cleaning Maintenance')
    type = models.CharField(choices=description.choices, max_length=11)
    superstructure = models.ForeignKey(Superstructure, on_delete=models.CASCADE)
