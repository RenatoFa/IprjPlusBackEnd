from django.urls import path
from accounts.views.user import RegisterView, UpdateProfileView
from accounts.views.login import LoginView
from accounts.views.otp import OTPView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/verify/', OTPView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profile/update/', UpdateProfileView.as_view(), name='update_profile')
]
