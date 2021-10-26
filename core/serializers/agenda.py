from rest_framework import serializers
from core.models import Agenda
from core.serializers.host import HostModelSerializer
from core.serializers.superstructure import SuperstructureModelSerializer


class AgendaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['host'] = HostModelSerializer(many=True, instance=instance.host).data

        return ret
