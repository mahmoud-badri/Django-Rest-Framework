from django.urls import path
from .views import HotelListCreateView, HotelRetrieveUpdateDestroyView

urlpatterns = [
    path('', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('<int:pk>/', HotelRetrieveUpdateDestroyView.as_view(), name='hotel-retrieve-update-destroy'),
]
