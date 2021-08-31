from django.urls import path

from .views import DogsListView, DogDetailView, AddDogView, UpdateDogView, DeleteDogView, ActivitiesListView, ActivityDetailView, AddActivityView, UpdateActivityView, DeleteActivityView

urlpatterns = [
    path('dogs', DogsListView.as_view(), name='dog-list'),
    path('dog/<int:pk>', DogDetailView.as_view(), name='dog-detail'),
    path('dog/add', AddDogView.as_view(), name='add-dog'),
    path('dog/<int:pk>/edit', UpdateDogView.as_view(), name='edit-dog'),
    path('dog/<int:pk>/delete', DeleteDogView.as_view(), name='delete-dog'),

    path('activities', ActivitiesListView.as_view(), name='activity-list'),
    path('activity/<int:pk>', ActivityDetailView.as_view(), name='activity-detail'),
    path('activity/add', AddActivityView.as_view(), name='add-activity'),
    path('activity/<int:pk>/edit', UpdateActivityView.as_view(), name='edit-activity'),
    path('activity/<int:pk>/delete', DeleteActivityView.as_view(), name='delete-activity'),

]