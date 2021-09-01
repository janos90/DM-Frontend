from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from members.forms import SignUpForm, EditProfileForm


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UserProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
