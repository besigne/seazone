from django.db import models


class Superstructure(models.Model):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
