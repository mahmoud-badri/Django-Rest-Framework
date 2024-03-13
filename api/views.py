from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import UserSerializer
from users.models import User
# Create your views here.


class UserView(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()