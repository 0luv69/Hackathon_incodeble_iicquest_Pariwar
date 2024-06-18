from rest_framework import serializers
from django.contrib.auth.models import User
from main_app.models import *
from django.core.exceptions import ObjectDoesNotExist

#   --------------------------   Accounts Api serializers -----------------------

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



# ---------------------------------Profile Api Serializers--------------------------------------------------------

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['user', 'email_token', 'is_verified', 'age', 'character']
        
        def create(self, validated_data):
            profile = ProfileModel.objects.create(
                user=validated_data.pop['user'],
                email_token=validated_data.pop['email_token'],
                is_verified=validated_data.pop['is_verified'],
                age=validated_data.pop['age'],
                character=validated_data.pop['character']
            )
            return profile

class GetProfile_Serializers(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    id = serializers.IntegerField(source='user.id', read_only=True)
    class Meta:
        model = ProfileModel
        fields = ['id', 'username', 'email', 'is_verified', 'age', 'character']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# -----------------------------------Issue Serializers Segment-----------------------------------------

class PostIssueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = IssueModel
        fields = ['id', 'title', 'description', 'preferred_char']
    
    def create(self, validated_data):
        id = validated_data.pop('id')
        try:
            user = User.objects.get(id=id)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        issuemodel = IssueModel.objects.create(issued_by=user, **validated_data)
        issue_serilizer = IssueSerializer(issuemodel)
        return issue_serilizer

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueModel
        fields= '__all__'


# ------------------------- Reply / Suggestion Serializers Segment----------------------------- 

class ReplySerializer(serializers.ModelSerializer):
    replied_by = UserSerializer(read_only=True)

    class Meta:
        model = ReplyModel
        fields = ['id', 'message', 'created_at', 'updated', 'replied_by', 'issued_by']
    
class PostReplySerializer(serializers.ModelSerializer):
    issued_id = serializers.IntegerField()
    reply_user_id = serializers.IntegerField()
    class Meta:
        model = ReplyModel
        fields = ['issued_id','reply_user_id', 'message']
    
    def validate(self, attrs):
        issued_id = attrs['issued_id']
        reply_user_id = attrs['reply_user_id']
        
        # Check if a reply with the same issued_id and reply_user_id already exists
        if ReplyModel.objects.filter(issued_by=issued_id, replied_by=reply_user_id).exists():
            raise serializers.ValidationError("A reply for this issue by this user already exists.")
        
        return attrs
    
    def create(self, validated_data):
        issued_id = validated_data.pop('issued_id')
        reply_user_id = validated_data.pop('reply_user_id')
        try:
            issued_user = IssueModel.objects.get(id = issued_id)
            user_reply = User.objects.get(id = reply_user_id)

        except ObjectDoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        replymodel = ReplyModel.objects.create(issued_by=issued_user,replied_by=user_reply, **validated_data)
        reply_serilizer = ReplySerializer(replymodel)
        return reply_serilizer
    

#       -------------------------- Relation Serializers ----------------------
class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationModel
        fields = '__all__'


#      ------------------------ Chat Segment ----------------------
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = [ 'sender', 'receiver', 'message', 'relation']
        
        def create(self, validated_data):
            # print(validated_data)
            chat = ChatModel.objects.create(
                sender=validated_data.pop['sender'],
                receiver=validated_data.pop['receiver'],
                message=validated_data.pop['message'],
                relation_id = validated_data.pop['id']
            )
            return chat
        
class ChatSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = ChatModel
        fields = ['username','sender', 'message', 'relation','date']




