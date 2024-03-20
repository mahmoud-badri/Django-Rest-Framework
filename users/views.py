from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, ImageSerializer
from .models import User, Image
import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, DecodeError
from django.shortcuts import redirect
from rest_framework.decorators import api_view


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


@api_view(['GET'])
def ImageList(request, hotel_id):
    all_images = Image.objects.filter(user=hotel_id)
    image_ser = ImageSerializer(all_images, many=True)
    return Response(image_ser.data)


@api_view(['GET'])
def ImageDetail(request, image_id):
    image_instance = Image.objects.get(id=image_id)
    image_ser = ImageSerializer(image_instance)
    return Response(image_ser.data)


@api_view(['POST'])
def ImageAdd(request):
    image_ser = ImageSerializer(data=request.data)
    if image_ser.is_valid():
        image_ser.save()
        return Response(image_ser.data, status=201)
    return Response(image_ser.errors, status=400)


@api_view(['PUT'])
def ImageEdit(request, image_id):
    image_instance = Image.objects.get(id=image_id)
    image_ser = ImageSerializer(instance=image_instance, data=request.data)
    if image_ser.is_valid():
        image_ser.save()
        return Response(image_ser.data)
    return Response(image_ser.errors, status=400)


@api_view(['DELETE'])
def ImageDelete(request, image_id):
    image_instance = Image.objects.get(id=image_id)
    image_instance.delete()
    return Response('The image was deleted successfully', status=204)
