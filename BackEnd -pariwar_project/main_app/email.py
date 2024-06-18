
#Import Email & Setting
from django.conf import settings
from django.core.mail import send_mail

# Import Module Segment
from django.contrib.auth.models import User
from main_app.serializer import *
from main_app.models import *


# Import Api Segment
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status






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
