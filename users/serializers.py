from rest_framework import serializers
from .models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from rest_framework import serializers

from send.utils import send_custom_email
from .models import User,image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'email','name','type','password' , 'confirm_password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'
