from django.urls import path, include
from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginApi.as_view(), name='login'),

    path('register/', RegisterApi.as_view(), name='register'),
    path('email-verify/', email_verify_token, name="email_verify_token"),

    path('get-profile/', get_profile, name='get_profile'),

    path('get-all-issue/', Get_All_Issue, name='Get_All_Issue'),
    path('get-issue/', Get_Issue, name='Get_Reply_Given'),
    path('post-issue/', Post_Issue, name='Post_Issue'),
    path('get-issue-chareter/', Get_Issue_Charater, name='Get_Issue_Charater'),

    path('get-reply-issue/', get_issue_reply, name='get_issue_reply'),

    
    path ('get-specific-issue/', Get_spefic_Issue, name = 'Get_spefic_Issue'),
    
    path('post-reply/', Postreply, name='Post_reply'),


    path('relation-update/', relation, name='relation'),
    path('get-particular-relation/', get_particular_relation, name='get_particular_relation'),

    path('post-chat/', post_chat, name='chat'),
    path('get-chat/', get_chat, name='get_chat'),
    

]