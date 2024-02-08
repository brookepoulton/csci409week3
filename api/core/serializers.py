from rest_framework import serializers
from core.models import Airline

class AirlineSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Airline
        fields = ['name', 'airline_code']