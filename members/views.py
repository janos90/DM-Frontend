from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, UpdateView


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UserProfileView(UpdateView):
    form_class = UserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
