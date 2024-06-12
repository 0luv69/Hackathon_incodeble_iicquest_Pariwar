from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import *



class RegisterUserSerializer(serializers.ModelSerializer):
    email_token = serializers.CharField(write_only=True, required=True)
    is_owner = serializers.BooleanField()
    class Meta:
        model = User
        fields = ['email', 'password','age','charater','email_token']

    def create(self, validated_data):
        email_token = validated_data.pop('email_token')
        age= validated_data.pop('age')
        charater= validated_data.pop('charater')
        username_as_email = validated_data.pop('email')

        user = User.objects.create_user(username=username_as_email,email=username_as_email, **validated_data)
        profile = Profile.objects.create(user=user, email_token= email_token,age=age, charater=charater)
    
        return user