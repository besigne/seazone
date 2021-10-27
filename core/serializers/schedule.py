from rest_framework import serializers
from core.models.schedule import Schedule


class ScheduleModelSerializer(serializers.ModelSerializer):
    checkIn = serializers.DateField(format=None, input_formats=['%Y-%m-%d %H:%M:%S'])
    checkOut = serializers.DateField(format=None, input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Schedule
        fields = '__all__'
