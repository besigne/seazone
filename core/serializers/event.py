from rest_framework import serializers
from core.models.event import Event


class EventModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        