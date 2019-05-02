from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_recipe, name='upload'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^accounts/update/', views.edit, name='update_profile'),
    url(r'^chefs', views.all_chefs, name='chefs'),
    url(r'^recipes', views.all_recipes, name='recipes'),
    url(r'^search/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
