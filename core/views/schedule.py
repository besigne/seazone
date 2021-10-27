from rest_framework.viewsets import ModelViewSet
from core.models.schedule import Schedule
from core.serializers.schedule import ScheduleModelSerializer


class ScheduleModelViewSet(ModelViewSet):

    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer
