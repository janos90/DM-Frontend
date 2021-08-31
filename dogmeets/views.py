from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dogmeets.forms import DogForm, ActivityForm
from dogmeets.models import Dog, Activity


# Create your views here.
class DogsListView(ListView):
    model = Dog
    template_name = 'dogs.html'


class DogDetailView(DetailView):
    model = Dog
    template_name = 'dog_detail.html'


class AddDogView(CreateView):
    model = Dog
    template_name = 'add_dog.html'
    form_class = DogForm


class UpdateDogView(UpdateView):
    model = Dog
    template_name = 'edit_dog.html'
    form_class = DogForm


class DeleteDogView(DeleteView):
    model = Dog
    template_name = 'delete_dog.html'
    success_url = reverse_lazy('dogs-list')


class ActivitiesListView(ListView):
    model = Activity
    template_name = 'activities.html'


class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'activity_detail.html'


class AddActivityView(CreateView):
    model = Activity
    template_name = 'add_activity.html'
    form_class = ActivityForm


class UpdateActivityView(UpdateView):
    model = Activity
    template_name = 'update_activity.html'
    form_class = ActivityForm


class DeleteActivityView(DeleteView):
    model = Activity
    template_name = 'delete_activity.html'
    success_url = reverse_lazy('dogs-list')
