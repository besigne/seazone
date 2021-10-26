from rest_framework.viewsets import ModelViewSet
from core.models.host import Host
from core.serializers.host import HostModelSerializers


class HostModelViewSet(ModelViewSet):

    queryset = Host.objects.all()
    serializer_class = HostModelSerializers
