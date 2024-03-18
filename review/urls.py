from django.urls import path
from review.views import *


urlpatterns = [
     
    path('reviews', create_review,name='create_review'),
    path('reviews/delete', delete_review,name='delete_review'),
]