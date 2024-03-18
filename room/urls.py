from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/<hotel_id>',RoomList,name='RoomList'),
    path('<room_id>',RoomDetail,name='RoomDetail'),
    path('add/',RoomAdd,name='RoomAdd'),
    path('edit/<room_id>',RoomEdit,name='RoomEdit'),
    path('delete/<room_id>',RoomDelete,name='RoomDelete'),

    path('facility/<room_id>',FacilityList,name='FacilityList'),
    path('facility<facility_id>',FacilityDetail,name='FacilityDetail'),
    path('facility/add',FacilityAdd,name='FacilityAdd'),
    path('facility/edit/<facility_id>',FacilityEdit,name='FacilityEdit'),
    path('facility/delete/<facility_id>',FacilityDelete,name='FacilityDelete'),
]
