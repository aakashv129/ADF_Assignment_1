"""URLS PAGE"""
#pylint: disable=relative-beyond-top-level
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home')
]
