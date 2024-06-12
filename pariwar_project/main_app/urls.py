from django.urls import path, include
from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', LoginApi.as_view(), name='login'),

    # path('register/', RegisterApi.as_view(), name='register'),
    # path('email-verify/', email_verify_token, name="email_verify_token"),


    # path('product/', ProductApi.as_view(), name='ProductApi'),
    # path('get-product/', get_product, name='get_product'),
]