from rest_framework import serializers, viewsets
from rest_framework.serializers import HyperlinkedRelatedField
from .models import SolarYield 


class SolarYieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  SolarYield 
        fields = ["state", "pv_yield"]

    pv_yield = serializers.SerializerMethodField()

    def get_pv_yield(self, obj):
        multiplied_value = self.context['request'].query_params.get('capacity', None)
        if multiplied_value:
            try:
                return obj.value * float(multiplied_value)
            except ValueError:  # in case the value is not a valid float
                return None
        return obj.value 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['yield'] = representation.pop('pv_yield')
        return representation

class SolarYieldViewSet(viewsets.ModelViewSet):
    queryset = SolarYield.objects.filter(country="de")
    serializer_class = SolarYieldSerializer 
    filterset_fields = ["state", "capacity"]