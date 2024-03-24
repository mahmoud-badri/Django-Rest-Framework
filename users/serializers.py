from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from rest_framework import serializers

from send.utils import send_custom_email
from .models import User,image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'name','type', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        subject = 'Welcome to Our Website!'
        message = ("Your account has been created. You can now log in to our website. "
                   "from this link: http://localhost:3000/Login")
        send_custom_email(subject, message, instance.email)
        print(instance)
        return instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'