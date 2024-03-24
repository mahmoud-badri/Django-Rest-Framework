from django.urls import path
from .views import *

urlpatterns = [
    
    path('api/succ/mail', MailSuccessfully.as_view(), name='MailSuccessfully'),
    path('api/rej/mail', MailFaild.as_view(), name='MailFaild'),
    
]