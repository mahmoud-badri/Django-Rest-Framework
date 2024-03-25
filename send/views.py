from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import IsAuthenticated
from django.contrib.auth.models import User  # Import User model
import json

from send.utils import send_custom_email


class MailSuccessfully(APIView):
    permission_classes = [AllowAny]  # Add IsAuthenticated permission
    
    def post(self, request):
        #user_email = request.user.email  # Get the email of the authenticated user
        body = json.loads(request.body)
        email_subject = 'TicTac Hotel Support'
        email_body = 'Your Booking Is Successfully. Please click <a href="https://www.paypal.com/eg/home">here</a> to go to PayPal for payment.'
        send_custom_email(email_subject, email_body, body.get('email'))
        # email_message = EmailMessage(
        #     email_subject,
        #     email_body,
        #     settings.EMAIL_HOST_USER,  # Sender's email
        #     [body.get("email")]  # Receiver's email
        #
        # )
        # email_message.send(fail_silently=False)
        return Response({'status': True, 'message': 'Email sent successfully'})


class MailFaild(APIView):
    permission_classes = [AllowAny]  # Add IsAuthenticated permission
    
    def post(self, request):
        #user_email = request.user.email  # Get the email of the authenticated user
        body=json.loads(request.body)
        email_subject = 'TicTac Hotel Support'
        email_body = "We apologize, but we're unable to process your booking request at this time. Please contact support for further assistance."
        
        email_message = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,  # Sender's email
            [body.get("email")]  # Receiver's email
            
        )
        email_message.send(fail_silently=False)
        return Response({'status': True, 'message': 'Email sent successfully'})