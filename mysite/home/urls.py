from django.urls import path
from . import views

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index.html', views.index, name='index.html'),

    path('elements', views.elements, name = 'elements'),
    path('elements.html', views.elements, name = 'elements.html'),

    path('generic', views.generic, name = 'generic'),
    path('generic.html', views.generic, name = 'generic.html'),

    path('about', views.about, name = 'about'),
    path('about.html', views.about, name = 'about.html'),
]

urlpatterns += staticfiles_urlpatterns()
