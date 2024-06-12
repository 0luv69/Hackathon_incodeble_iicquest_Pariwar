from django.shortcuts import render
import random
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view


from main_app.serializer import *
from main_app.models import *


from django.conf import settings
from django.core.mail import send_mail


from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


# # Accounts Api 
class LoginApi(APIView):
    def post(self, request):
        data = request.data 
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'message': 'username & password Fields is required', 'login': False}, status=status.HTTP_400_BAD_REQUEST)
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'posted': True,
                'user_id': user.pk,
                'user_name': user.username,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials', 'posted':False}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterApi(APIView):
    def post(self, request):
        data = request.data 
        email_token = str(random.randint(1000, 9999)) 
        data['email_token'] = email_token
        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            send_account_activation_email(user.email, email_token, user)
            return Response({'posted':True, 'id': user.id})
        
        elif 'username' in serializer.errors and serializer.errors['username'][0].code == 'unique':
            return Response({"message": "Username already exists", "posted": False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": serializer.errors, "posted": False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def email_verify_token(request):
    data = request.data
    id = data.get('id')
    email_token = data.get('email_token')
    
    try:
        user = User.objects.get(id = id)
        bio_obj = ProfileModel.objects.get(user__id=id, email_token=email_token)
        bio_obj.is_verified = True
        bio_obj.save()

        refresh = RefreshToken.for_user(user)  # Generate JWT token
        return Response({
                'verified': True,
                'id': user.pk,
                'username':user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

    except User.DoesNotExist:
        return Response({
            'verified':False,
            'message': 'Invalid id or email_token',
        }, status=403)
    except Exception as e:
        return Response({
            'verified':False,
            'message': f'An unexpected error occurred,{e}'
        }, status=500)

def send_account_activation_email(email, email_token, complaint_instance):
    subject= 'lets verify so click the link plz'
    email_from = settings.EMAIL_HOST_USER
    message = f'''Hi, {complaint_instance.username} Your authentation Otp Code is : 
    
    {email_token}
    thanks
'''
    send_mail(subject, message, email_from, [email])




# # Issue 
@api_view(['POST'])
def Post_Issue(request):
        data = request.data
    # if data:
        serializer = PostIssueSerializer(data=data)
        if serializer.is_valid():
            serl =serializer.save()
            return Response({'success':True, "payload": serl })
        else:
            return Response({'success':False, "error" :serializer.errors})
    
@api_view(['POST'])
def Get_Issue(request):
    data = request.data
    if data:
        try:
            id = data.get('id')
            issuemodel = IssueModel.objects.filter(issued_by__id= id)
            serializer = IssueSerializer(issuemodel, many = True)
            return Response({'success':True, "payload": serializer.data})
        except Exception as e:
            return Response({'success':False, "message": e, "hint": "Incorrect id of user"})
    return Response({'success':False, "message": "Got None or Incorrect id of user"})
        


# # reply






