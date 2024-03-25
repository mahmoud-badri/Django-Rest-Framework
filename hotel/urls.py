from django.urls import path
from .views import *

urlpatterns = [
    
    path('', HotelList.as_view(), name='HotelList'),
    path('add/',HotelAdd,name='HotelAdd'),
    path('<hotel_id>/',HotelDetail,name='HotelDetail'),
    path('delete/<hotel_id>',HotelDelete,name='HotelDelete'),
    # path('', HotelListCreateView.as_view(), name='hotel-list-create'),
    # path('<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel-retrieve-update-destroy'),
    path('booking', BookingListCreateView, name='booking-list-create'),
    path('bookingList', BookList.as_view(), name='HotelList'),
    path('BookingBasedHotel/<hotel_id>', BookingBasedHotel, name='BookingBasedHotel'),

    path('booking_customer',booking_customer,name='my_booking'),
    path('booking_by_hotel_owner/<id>/',booking_by_hotel_owner,name='booking_by_hotel_owner'),
    path('confirm_booking/<id>/',confirm_booking,name='confirm_booking'),
    path('reject_booking/<id>/',reject_booking,name='reject_booking'),

    # path('booking/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-retrieve-update-destroy'),
]
