from django.urls import path, include
from user_app.api.views import registration_view, GenerateInviteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('generateinvite/', GenerateInviteView.as_view(), name="generate-invite"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
