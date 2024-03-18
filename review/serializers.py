from rest_framework import serializers
from .models import Review


def get_reviews(self,obj):
    reviews = obj.reviews.all()
    serializer = ReviewSerializer(reviews,many=True)
    return serializer.data

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'