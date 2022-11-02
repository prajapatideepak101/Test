from django.urls import path
from account.views import UserRegistrationView,UserLoginView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('Login/', UserLoginView.as_view(),name='Login'),
    
]
