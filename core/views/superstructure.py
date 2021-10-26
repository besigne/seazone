from rest_framework.viewsets import ModelViewSet
from core.models.superstructure import Superstructure
from core.serializers.superstructure import SuperstructureModelSerializer


class SuperstructureModelViewSet(ModelViewSet):

    queryset = Superstructure.objects.all()
    serializer_class = SuperstructureModelSerializer
