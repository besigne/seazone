from rest_framework import serializers
from core.models.event import Event


class EventModelSerializer(serializers.ModelSerializer):
    checkIn = serializers.DateField(format=None, input_formats=['%Y-%m-%d %H:%M:%S'])
    checkOut = serializers.DateField(format=None, input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Event
        fields = '__all__'
