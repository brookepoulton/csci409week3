from rest_framework import serializers
from core.models import Airline, Airport, Runway, Flights

class AirlineSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Airline
        fields = ['airport', 'airline_code']
        read_only_fields = ['id']