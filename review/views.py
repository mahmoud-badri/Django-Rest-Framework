from django.shortcuts import render
from .models import Review
from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from django.db.models import Avg

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request,pk):
    user = request.user
    hotel = get_object_or_404(hotel,id=pk)
    data = request.data
    review = hotel.reviews.filter(user=user)
   
    if data['rating'] <= 0 or data['rating'] > 10:
        return Response({"error":'Please select between 1 to 5 only'}
                        ,status=status.HTTP_400_BAD_REQUEST) 
    elif review.exists():
        new_review = {'rating':data['rating'], 'comment':data['comment'] }
        review.update(**new_review)

        rating = hotel.reviews.aggregate(avg_ratings = Avg('rating'))
        hotel.ratings = rating['avg_ratings']
        hotel.save()

        return Response({'details':'Hotel review updated'})
    else:
        Review.objects.create(
            user=user,
            hotel=hotel,
            rating= data['rating'],
            comment= data['comment']
        )
        rating = hotel.reviews.aggregate(avg_ratings = Avg('rating'))
        hotel.ratings = rating['avg_ratings']
        hotel.save()
        return Response({'details':'hotel review created'})
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request,pk):
    user = request.user
    hotel = get_object_or_404(hotel,id=pk)
   
    review = hotel.reviews.filter(user=user)
   
 
    if review.exists():
        review.delete()
        rating = hotel.reviews.aggregate(avg_ratings = Avg('rating'))
        if rating['avg_ratings'] is None:
            rating['avg_ratings'] = 0
            hotel.ratings = rating['avg_ratings']
            hotel.save()
            return Response({'details':'Product review deleted'})
    else:
        return Response({'error':'Review not found'},status=status.HTTP_404_NOT_FOUND)


