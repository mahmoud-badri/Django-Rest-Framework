from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.db.models import Avg
from .serializers import *
from hotel.models import *
from .models import *
from rest_framework import generics

class ListRates(generics.ListAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer



class CreateRates(generics.CreateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    # permission_classes = [IsAuthenticated]  -->Uncomment for authentication
    # permission_classes = (CustomPermission,)


class GetRateById(generics.RetrieveAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'


class DeleteRateById(generics.DestroyAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'
    # permission_classes = [IsAuthenticated] -->Uncomment for authentication
    # permission_classes = (CustomPermission,)

# PAtch method
class UpdateRateById(generics.UpdateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'

@api_view(['GET'])
def allRates(req,id):
    all_rates=Rate.objects.filter(hotel=id)
    data= RateSerializer(all_rates,many=True).data
    return Response ({'data':data})