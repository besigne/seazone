from django.db import models
from core.models.host import Host


class Agenda(models.Model):
    host = models.ManyToManyField(Host)
