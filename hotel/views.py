from django.shortcuts import render
from rest_framework import generics
from .models import Hotel
from .serializers import  HotelSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect

@api_view(['Get'])
def HotelList(request):
    all_hotels = Hotel.objects.all()
    hotel_ser = HotelSerializer(all_hotels,many=True)
    return Response(hotel_ser.data)

@api_view(['Get'])
def HotelDetail(request,hotel_id):
    hotel = Hotel.objects.get(id = hotel_id )
    hotel_ser = HotelSerializer(hotel,many=False)
    return Response(hotel_ser.data)

@api_view(['POST'])
def HotelAdd(request):
    hotel_ser = HotelSerializer(data=request.data)
    if hotel_ser.is_valid():
        hotel_ser.save()
        return redirect('HotelList')

@api_view(['POST'])
def HotelEdit(request,hotel_id):
    hotel = Hotel.objects.get(id = hotel_id )
    hotel_ser = HotelSerializer(data=request.data,instance=hotel)
    if hotel_ser.is_valid():
        hotel_ser.save()
        return redirect('HotelList')

@api_view(['DELETE'])
def HotelDelete(request,hotel_id):
    hotel = Hotel.objects.get(id = hotel_id )
    hotel.delete()
    return Response('hotel deleted successfully')
