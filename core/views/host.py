from rest_framework.viewsets import ModelViewSet
from core.models import Superstructure, Schedule
from core.models.host import Host
from core.serializers.host import HostModelSerializer
from django.http import JsonResponse

from core.serializers.schedule import ScheduleModelSerializer
from core.serializers.superstructure import SuperstructureModelSerializer


class HostModelViewSet(ModelViewSet):

    queryset = Host.objects.all()
    serializer_class = HostModelSerializer

    def get_agenda(self, request, host_id):
        host = Host.objects.filter(id=host_id).first()
        serializer = HostModelSerializer(host)
        response = serializer.data['schedule']
        return JsonResponse(response, safe=False)

