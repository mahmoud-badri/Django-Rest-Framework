from django.conf import settings
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from payment.utils import payment_key_request
from .models import Hotel, Booking
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect

from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
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
    hotels = Hotel.objects.filter(user_id=id)
    if hotels.exists():
        bookings = []
        for hotel in hotels:
            bookings.extend(hotel.booking_set.all())
        booking_ser = BookingHotelSerializer(bookings, many=True)
        return Response(booking_ser.data)
    else:
        return Response("No hotel found for this owner ID", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def confirm_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    payment_url = payment_key_request(booking.user, booking.hotel.get_amount())
    booking.is_accepted = True
    booking.save()
    subject = 'Complete Your Hotel Reservation Payment'
    message = f'Please complete your payment by clicking the link below:\n\n{payment_url}'
    recipient_email = booking.user.email  # Change to the user's email
    
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
    return Response('Booking confirmed successfully')


@api_view(['POST'])
def reject_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.is_accepted = False
    booking.save()
    subject = 'Information About Your Hotel Reservation'
    message = 'Your hotel reservation has been rejected please try to reserve another hotel'
    recipient_email = booking.user.email  # Change to the user's email

    send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
    return Response('Booking rejected successfully')