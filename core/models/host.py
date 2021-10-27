from django.db import models
from core.models import Schedule


class Host(models.Model):
    name = models.CharField(max_length=40)
    CPF = models.CharField(max_length=11)
    schedule = models.ManyToManyField(Schedule)
