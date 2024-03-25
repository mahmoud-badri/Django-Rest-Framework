# serializers.py

from rest_framework import serializers
from .models import Hotel, Booking
from users.serializers import UserSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        booking = Booking.objects.create(**validated_data)
        return booking
    
class BookingHotelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
