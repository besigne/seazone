from rest_framework import serializers
from core.models.agenda import Agenda


class AgendaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = ['host_id', 'event_id']
