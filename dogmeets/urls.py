from django.urls import path

from .views import DogsListView, DogDetailView, AddDogView, UpdateDogView, DeleteDogView

urlpatterns = [
    path('dogs', DogsListView.as_view(), name='dog-list'),
    path('dog/<int:pk>', DogDetailView.as_view(), name='dog-detail'),
    path('dog/add', AddDogView.as_view(), name='add-dog'),
    path('dog/<int:pk>/edit', UpdateDogView.as_view(), name='edit-dog'),
    path('dog/<int:pk>/delete', DeleteDogView.as_view(), name='delete-dog'),
]