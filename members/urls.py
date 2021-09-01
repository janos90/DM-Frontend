from django.urls import path
from .views import UserRegisterView, UserProfileView, PasswordsChangeView
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', views.password_success, name='password_success')
]
