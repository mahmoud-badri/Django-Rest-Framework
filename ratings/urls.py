# In your main project's urls.py
from django.urls import path, include
from ratings import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ratings', views.RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
]
