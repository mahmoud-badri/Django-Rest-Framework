from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from project import settings
from .serializers import UserSerializer, ImageSerializer
from .models import User,image
import jwt, datetime
from jwt.exceptions import ExpiredSignatureError, DecodeError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.exceptions import APIException
#from .email_utils import send_activation_email
class ActivateAccount(APIView):
    def get(self, request, token):
        try:
            # Decode the activation token
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token['user_id']
            
            # Fetch the user from the database
            user = User.objects.get(id=user_id)
            
            # Update the email_verified field
            user.email_verified = True
            user.save()
            
            # Return a success message or redirect the user to a page confirming activation
            return HttpResponse({ '<h1 >Your account has been successfully activated.</h1>'})
        except jwt.ExpiredSignatureError:
            return HttpResponse({ '<h1 >Activation link has expired.</h1>'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return HttpResponse({ '<h1 >Invalid token.</h1>'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return HttpResponse({ '<h1 >User not found.</h1>'}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate activation token
        activation_token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        # Send activation email
        activation_link = f"{settings.BASE_URL}api/activate/{activation_token}"
        subject = 'Activate Your Account'
        message = f'Hi {user.name},\n\nPlease click the link below to activate your account:\n{activation_link}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        try:
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            # Handle email sending failure
            raise APIException('Failed to send activation email.')

        return Response({'message': 'User created successfully. Please check your email to activate your account.'})

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        serializer = UserSerializer(user)
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        if not user.email_verified:
            raise AuthenticationFailed('Email not verified! Please verify your email.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
            
        }
        response.data['user'] = serializer.data
    
        return response



class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except DecodeError:
            raise AuthenticationFailed('Invalid token!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

@api_view(['Get'])
def ImageList(request,hotel_id):
    all_images = image.objects.filter(user=hotel_id)
    image_ser = ImageSerializer(all_images,many=True)
    return Response(image_ser.data)

@api_view(['Get'])
def ImageDetail(request,image_id):
    image = image.objects.get(id = image_id )
    image_ser = ImageSerializer(image,many=False)
    return Response(image_ser.data)

@api_view(['POST'])
def ImageAdd(request):
    image_ser = ImageSerializer(data=request.data)
    if image_ser.is_valid():
        image_ser.save()
        # return redirect('imageList')
    return Response(image_ser.data)


@api_view(['POST'])
def ImageEdit(request,image_id):
    images = image.objects.get(id = image_id )
    image_ser = ImageSerializer(data=request.data,instance=images)
    if image_ser.is_valid():
        image_ser.save()
        return redirect('ImageList')

@api_view(['DELETE'])
def ImageDelete(request,image_id):
    image = image.objects.get(id = image_id )
    image.delete()
    return Response('the image deleted successfully')
