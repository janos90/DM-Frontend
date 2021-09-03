from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    bio = RichTextField(blank=True, null=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    birthday = models.DateField()
    anniversary = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/dog-profiles")

    def __str__(self):
        return self.name + " " + self.breed

    def get_absolute_url(self):
        return reverse('dog-detail', args=(str(self.id)))


class Activity(models.Model):
    name = models.CharField(max_length=255)
    creationDate = models.DateField(auto_now_add=True)
    startTime = models.DateField()
    location = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    dogs = models.ManyToManyField(Dog)

    def get_absolute_url(self):
        return reverse('activity-detail', args=(str(self.id)))
