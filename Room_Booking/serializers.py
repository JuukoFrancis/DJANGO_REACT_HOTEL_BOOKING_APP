from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    name
    type
    pricePerNIght
    currency
    maxOccupancy
    description    
