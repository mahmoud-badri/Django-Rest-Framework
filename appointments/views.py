from django.shortcuts import render
from rest_framework import generics
from .models import Appointment
from .serializers import  AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect

@api_view(['Get'])
def AppointmentList(request):
    all_appoints = Appointment.objects.all()
    appoint_ser = AppointmentSerializer(all_appoints,many=True)
    return Response(appoint_ser.data)

@api_view(['Get'])
def AppointmentDetail(request,appoint_id):
    appoint = Appointment.objects.get(id = appoint_id )
    appoint_ser = AppointmentSerializer(appoint,many=False)
    return Response(appoint_ser.data)

@api_view(['POST'])
def AppointmentAdd(request):
    appoint_ser = AppointmentSerializer(data=request.data)
    if appoint_ser.is_valid():
        appoint_ser.save()
        return redirect('AppointmentList')

@api_view(['POST'])
def AppointmentEdit(request,appoint_id):
    appoint = Appointment.objects.get(id = appoint_id )
    appoint_ser = AppointmentSerializer(data=request.data,instance=appoint)
    if appoint_ser.is_valid():
        appoint_ser.save()
        return redirect('AppointmentList')

@api_view(['DELETE'])
def AppointmentDelete(request,appoint_id):
    appoint = Appointment.objects.get(id = appoint_id )
    appoint.delete()
    return Response('appointment deleted successfully')
