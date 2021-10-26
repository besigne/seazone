from rest_framework.viewsets import ModelViewSet
from core.models.host import Host
from core.serializers.host import HostModelSerializer


class HostModelViewSet(ModelViewSet):

    queryset = Host.objects.all()
    serializer_class = HostModelSerializer
