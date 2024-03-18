from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect



#room
# @api_view(['Get'])
# def HotelList(request):
#     all_hotels = User.objects.all()
#     hotel_ser = UserSerializer(all_hotels,many=True)
#     return Response(hotel_ser.data)
    
@api_view(['Get'])
def RoomList(request,hotel_id):
    all_rooms = Room.objects.filter(hotel=hotel_id)
    room_ser = RoomSerializer(all_rooms,many=True)
    return Response(room_ser.data)

@api_view(['Get'])
def RoomDetail(request,room_id):
    room = Room.objects.get(id = room_id )
    room_ser = RoomSerializer(room,many=False)
    return Response(room_ser.data)

@api_view(['POST'])
def RoomAdd(request):
    room_ser = RoomSerializer(data=request.data)
    if room_ser.is_valid():
        room_ser.save()
        # return redirect('RoomList')
    return Response(room_ser.data)


@api_view(['POST'])
def RoomEdit(request,room_id):
    rooms = Room.objects.get(id = room_id )
    room_ser = RoomSerializer(data=request.data,instance=rooms)
    if room_ser.is_valid():
        room_ser.save()
        return redirect('RoomList')

@api_view(['DELETE'])
def RoomDelete(request,room_id):
    room = Room.objects.get(id = room_id )
    room.delete()
    return Response('the room deleted successfully')


#facility
@api_view(['Get'])
def FacilityList(request,room_id):
    all_facilities = Facility.objects.filter(room=room_id)
    facility_ser = FacilitySerializer(all_facilities,many=True)
    return Response(facility_ser.data)

@api_view(['Get'])
def FacilityDetail(request,facility_id):
    facility = Facility.objects.get(id = facility_id )
    facility_ser = FacilitySerializer(facility,many=False)
    return Response(facility_ser.data)

@api_view(['POST'])
def FacilityAdd(request):
    facility_ser = FacilitySerializer(data=request.data)
    if facility_ser.is_valid():
        facility_ser.save()
        return redirect('FacilityList')

@api_view(['POST'])
def FacilityEdit(request,facility_id):
    facility = Facility.objects.get(id = facility_id )
    facility_ser = FacilitySerializer(data=request.data,instance=facility)
    if facility_ser.is_valid():
        facility_ser.save()
        return redirect('FacilityList')

@api_view(['DELETE'])
def FacilityDelete(request,facility_id):
    facility = Facility.objects.get(id = facility_id )
    facility.delete()
    return Response('the facility deleted successfully')
