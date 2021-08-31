from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from dogmeets.forms import DogForm
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
    template_name = 'update_post.html'
    form_class = DogForm


class DeleteDogView(DeleteView):
    model = Dog
    template_name = 'delete_dog.html'
    success_url = reverse_lazy('home')
