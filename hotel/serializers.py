# serializers.py

from rest_framework import serializers
from .models import Hotel, Booking,image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = ['img']

class HotelSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

