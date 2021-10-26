from django.db import models


class Event(models.Model):
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    event = models.TextChoices('Event', 'Cleaning Maintenance')
    type = models.CharField(choices=event.choices, max_length=11)
