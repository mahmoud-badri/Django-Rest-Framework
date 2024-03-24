from rest_framework import serializers
from .models import *



class RateSerializer(serializers.ModelSerializer):

    class Meta:
            model=Rate
            fields='__all__'