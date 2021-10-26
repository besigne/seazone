from rest_framework import serializers
from core.models.superstructure import Superstructure


class SuperstructureModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Superstructure
        fields = '__all__'
        