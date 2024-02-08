from rest_framework import serializers
from core.models import Airline, Runway, Flights

class AirlineSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Airline
        fields = ['name', 'airline_code']
        read_only_fields = ['id'] 

class RunwaySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Runway
        fields = ['airport', 'runway_number', 'runway_designation', 'length', 'width']
        read_only_fields = ['id']

class FlightsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Flights
        fields = ['origin','destination','airline','departure','arrival','flight_number','aicraft_type']
        read_only_fields = ['id']