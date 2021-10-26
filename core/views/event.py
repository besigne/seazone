from rest_framework.viewsets import ModelViewSet
from core.models.event import Event
from core.serializers.event import EventModelSerializer


class EventModelViewSet(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventModelSerializer
