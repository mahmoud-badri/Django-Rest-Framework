from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, ImageSerializer
from .models import User,image
import jwt, datetime
from jwt.exceptions import ExpiredSignatureError, DecodeError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'email already exists'}, status=400)
        
        # Create a new user
        user = User.objects.create_user(email=email, password=password)
        user.save()
        
        return JsonResponse({'message': 'Registration successful'})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


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

@api_view(['Get'])
def allUsers(request):
    all_Users = User.objects.all()
    User_ser = UserSerializer(all_Users,many=True)
    return Response(User_ser.data)

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
