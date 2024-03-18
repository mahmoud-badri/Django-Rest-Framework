from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

    path('images/<hotel_id>',ImageList,name='ImageList'),
    path('<image_id>',ImageDetail,name='ImageDetail'),
    path('add/',ImageAdd,name='ImageAdd'),
    path('edit/<image_id>',ImageEdit,name='ImageEdit'),
    path('delete/<image_id>',ImageDelete,name='ImageDelete'),

]
