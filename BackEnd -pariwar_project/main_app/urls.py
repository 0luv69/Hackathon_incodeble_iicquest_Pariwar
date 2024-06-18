from django.urls import path, include
from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # ------------------------- Jwt Token-----------------------------
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#   --------------------------   Accounts Api Urls -----------------------
    path('register/', RegisterApi.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('email-verify/', email_verify_token, name="email_verify_token"),


# ---------------------------------Profile Api--------------------------------------------------------
    path('get-profile/', get_profile, name='get_profile'),


# -----------------------------------Issue Segment-----------------------------------------
    path('post-issue/', Post_Issue, name='Post_Issue'),
    path('get-all-issue/', Get_All_Issue, name='Get_All_Issue'),
    path('get-issue-chareter/', Get_Issue_Charater, name='Get_Issue_Charater'),
    path('get-issue/', Get_Issue, name='Get_Reply_Given'),
    path ('get-specific-issue/', Get_spefic_Issue, name = 'Get_spefic_Issue'),


# ------------------------- Reply / Suggestion Segment----------------------------- 
    path('post-reply/', Postreply, name='Post_reply'),
    path('get-reply-issue/', get_issue_reply, name='get_issue_reply'),

    
    
#       -------------------------- Relation ----------------------
    path('relation-update/', relation_update, name='relation'),
    path('get-particular-relation/', get_particular_relation, name='get_particular_relation'),


#      ------------------------ Chat Segment ----------------------
    path('post-chat/', post_chat, name='chat'),
    path('get-chat/', get_chat, name='get_chat'),
    

]