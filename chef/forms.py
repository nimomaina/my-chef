from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('screenshot','title','description','chef','profile')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]


