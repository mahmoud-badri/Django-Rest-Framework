from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Hotel, Booking
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect

from rest_framework.views import APIView


from .pagination import CustomPagination
class HotelListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating hotels.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    #pagination_class = CustomPagination



    def create(self, request, *args, **kwargs):
        """
        Create a new hotel instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class HotelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting hotels.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
# class BookingListCreateView(APIView):
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

@api_view(['POST'])
def BookingListCreateView(request):
    hotel_ser = BookingSerializer(data=request.data)
    if hotel_ser.is_valid():
        hotel_ser.save()
        # return redirect('hotelList')
    return Response(hotel_ser.data)

class BookList(generics.ListAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

# class BookingListCreateView(generics.ListCreateAPIView):
#     """
#     API endpoint for listing and creating bookings.
#     """
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Add permission class

#     def create(self, request, *args, **kwargs):
#         """
#         Create a new booking instance.
#         """
#         if request.user.is_authenticated:  # Check if user is authenticated
            
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#         else:
#             return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

# class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     API endpoint for retrieving, updating, and deleting bookings.
#     """
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


# @api_view(['Get'])
# def HotelList(request):
#     # all_hotels = Hotel.objects.filter(status="Verified")
#     all_hotels = Hotel.objects.all()

#     hotel_ser = HotelSerializer(all_hotels,many=True)
#     return Response({"hotels":hotel_ser.data})
class HotelList(generics.ListAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer


@api_view(['Get'])
def HotelDetail(request,hotel_id):
    hotel = Hotel.objects.get(id = hotel_id )
    hotel_ser = HotelSerializer(hotel,many=False)
    return Response({"hotels":hotel_ser.data})

@api_view(['POST'])
def HotelAdd(request):
    hotel_ser = HotelSerializer(data=request.data)
    if hotel_ser.is_valid():
        hotel_ser.save()
        # return redirect('hotelList')
    return Response({"hotels":hotel_ser.data})


@api_view(['POST'])
def HotelEdit(request,hotel_id):
    hotels = Hotel.objects.get(id = hotel_id )
    hotel_ser = HotelSerializer(data=request.data,instance=hotels)
    if hotel_ser.is_valid():
        hotel_ser.save()
        return redirect('HotelList')

@api_view(['DELETE'])
def HotelDelete(request,hotel_id):
    hotel = Hotel.objects.get(id = hotel_id )
    hotel.delete()
    return Response('the hotel deleted successfully')

@api_view(['POST'])
def booking_customer(request):
    print("hello from booking add")
    booking_ser = BookingSerializer(data=request.data)
    if request.method == 'POST':
        if booking_ser.is_valid():
            booking_ser.save()
            return Response(booking_ser.data)
        return Response(booking_ser.errors)
    
@api_view(['GET'])
def booking_by_hotel_owner(request, id):
    
    hotel = Hotel.objects.get(user_id=id)
    bookings = hotel.booking_set.all()
    booking_ser = BookingHotelSerializer(bookings, many=True)
    return Response(booking_ser.data)


@api_view(['POST'])
def confirm_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.is_accepted = True
    booking.save()
    return Response('Booking confirmed successfully')

@api_view(['POST'])
def reject_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.is_accepted = False
    booking.save()
    return Response('Booking rejected successfully')