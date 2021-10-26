from rest_framework.viewsets import ModelViewSet
from core.models.agenda import Agenda
from core.serializers.agenda import AgendaModelSerializer


class AgendaModelViewSet(ModelViewSet):

    queryset = Agenda.objects.all()
    serializer_class = AgendaModelSerializer
