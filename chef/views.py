from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from . forms import *
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email

def home(request):
    profiles=Profile.objects.order_by('pk')[:4]
    recipes = Recipe.objects.order_by('-pk')[:4]
    return render(request, 'home.html',locals())

@login_required(login_url='/accounts/login/')
def upload_recipe(request):
    current_user = request.user
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.save()
            return redirect('home')
    else:
        form = RecipeForm()


    return render(request,'upload_recipe.html',locals())

# views for profile

@login_required(login_url='/accounts/login/')
def profile(request, username):
    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    user = request.user
    profile = User.objects.get(username=username)
    recipes = Recipe.objects.filter(chef_id = profile.id)
    print(profile_details)

    title = f'@{profile.username} '

    return render(request, 'profile.html', locals())



@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', locals())


def all_chefs(request):
    profiles=Profile.objects.all()
    return render(request,'chefs.html', locals())

def all_recipes(request):
    recipes=Recipe.objects.all()
    return render(request,'all_recipes.html', locals())

def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_project = Recipe.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

