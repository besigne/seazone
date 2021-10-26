from django.db import models
from core.models import Event, Superstructure


class Host(models.Model):
    name = models.CharField(max_length=40)
    CPF = models.CharField(max_length=11)
    event = models.ManyToManyField(Event)
    superstructure = models.ManyToManyField(Superstructure)
