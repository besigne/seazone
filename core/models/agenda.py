from django.db import models
from core.models.event import Event
from core.models.superstructure import Superstructure
from core.models.host import Host


class Agenda(models.Model):
    host_id = models.ManyToManyField(Host)
    event_id = models.ManyToManyField(Event)
    superstructure_id = models.ManyToManyField(Superstructure)
