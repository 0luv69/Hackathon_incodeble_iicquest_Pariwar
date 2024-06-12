from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import *
from django.core.exceptions import ObjectDoesNotExist


class RegisterUserSerializer(serializers.ModelSerializer):
    email_token = serializers.CharField(write_only=True, required=True)
    age = serializers.IntegerField()
    character = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password','age','character','email_token']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'required': True}}

    def create(self, validated_data):
        email_token = validated_data.pop('email_token')
        age= validated_data.pop('age')
        character= validated_data.pop('character')
        user = User.objects.create_user( **validated_data)
        profile = ProfileModel.objects.create(user=user, email_token= email_token,age=age, character=character)
    
        return user
    

class PostIssueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = IssueModel
        fields = ['id', 'title', 'description', 'prefered_char']
    
    def create(self, validated_data):
        id = validated_data.pop('id')
        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        issuemodel = IssueModel.objects.create(issued_by=user, **validated_data)
        return issuemodel

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueModel
        fields= '__all__'
    
