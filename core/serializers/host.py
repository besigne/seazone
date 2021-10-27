from rest_framework import serializers
from core.models.host import Host
from core.serializers.schedule import ScheduleModelSerializer


class HostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['schedule'] = ScheduleModelSerializer(many=True, instance=instance.schedule).data

        return ret
