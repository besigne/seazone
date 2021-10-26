from rest_framework import serializers
from core.models.host import Host
from core.serializers.event import EventModelSerializer
from core.serializers.superstructure import SuperstructureModelSerializer


class HostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['event'] = EventModelSerializer(many=True, instance=instance.event).data
        ret['superstructure'] = SuperstructureModelSerializer(many=True, instance=instance.superstructure).data

        return ret
