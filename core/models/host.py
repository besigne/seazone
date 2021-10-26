from django.db import models


class Host(models.Model):
    name = models.CharField(max_length=40)
    CPF = models.CharField(max_length=11)
