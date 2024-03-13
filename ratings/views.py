# ratings/views.py
from rest_framework import viewsets
from .models import Rating
from .serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
