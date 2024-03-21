from django.urls import path
from .views import *

urlpatterns = [
    path('', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel-retrieve-update-destroy'),
    # path('hotels/', HotelList, name='HotelList'),
    # path('add/',HotelAdd,name='HotelAdd'),
    # path('<hotel_id>/',HotelDetail,name='HotelDetail'),
    # path('delete/<hotel_id>',HotelDelete,name='HotelDelete'),

    path('booking/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('booking/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-retrieve-update-destroy'),
]
