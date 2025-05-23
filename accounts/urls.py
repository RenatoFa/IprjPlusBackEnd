from django.urls import path
from accounts.views.register import RegisterView
from accounts.views.login import LoginView
from accounts.views.otp import OTPView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('login/verify/', OTPView.as_view()),
]
