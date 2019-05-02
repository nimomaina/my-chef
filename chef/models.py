from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField


# Create your models here.


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null = True)



    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.filter(user=id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user=id).first()
        return details

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Recipe(models.Model):
    screenshot = ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=255)
    chef = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.ForeignKey(Profile)

    class Meta:
        ordering = ['-pk']

    def save_project(self):
        self.save()


    def delete_image(self):
        self.delete()

    def __str__(self):

        return self.title

    @classmethod
    def get_by_id(cls, id):
        details = Recipe.objects.filter(chef=id)
        return details

    @classmethod
    def get_all_projects(cls):
        project = Recipe.objects.all()
        return project

    @classmethod
    def search_by_project(cls, search_term):
        project = Recipe.objects.filter(title__icontains=search_term)
        return project

