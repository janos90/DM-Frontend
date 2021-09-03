from django.urls import path
from .views import UserRegisterView, UserSettingsView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page')

]
