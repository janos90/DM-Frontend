from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from dogmeets.models import Profile
from members.forms import SignUpForm, PasswordChangingForm, EditSettingsForm


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user-profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def password_success(request):
    return render(request, 'password_success.html', {})


class UserSettingsView(UpdateView):
    form_class = EditSettingsForm
    template_name = 'edit-settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'edit_profile_page.html'
    fields = ['image', 'bio', 'facebook_url', 'website_url', 'pinterest_url', 'twitter_url', 'instagram_url']
    success_url = reverse_lazy('login')

