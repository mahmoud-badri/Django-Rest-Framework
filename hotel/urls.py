from django.urls import path
from .views import HotelListCreateView, HotelRetrieveUpdateDestroyView, BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    path('', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel-retrieve-update-destroy'),
    path('booking/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('booking/<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-retrieve-update-destroy'),
]
