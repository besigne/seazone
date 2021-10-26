from rest_framework import serializers
from core.models.host import Host


class HostModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = '__all__'
