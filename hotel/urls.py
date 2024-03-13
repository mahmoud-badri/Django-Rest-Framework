from django.urls import path
from hotel.views import  *

urlpatterns = [
   
    path('',HotelList,name='HotelList'),
    path('<hotel_id>',HotelDetail,name='HotelDetail'),
    path('add',HotelAdd,name='HotelAdd'),
    path('edit/<hotel_id>',HotelEdit,name='HotelEdit'),
    path('delete/<hotel_id>',HotelDelete,name='HotelDelete'),

]