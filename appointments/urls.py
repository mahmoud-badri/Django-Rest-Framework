from django.urls import path
from .views import  *

urlpatterns = [
    path('',AppointmentList,name='AppointmentList'),
    path('<appoint_id>',AppointmentDetail,name='AppointmentDetail'),
    path('add/',AppointmentAdd,name='AppointmentAdd'),
    path('edit/<appoint_id>',AppointmentEdit,name='AppointmentEdit'),
    path('delete/<appoint_id>',AppointmentDelete,name='AppointmentDelete'),
]