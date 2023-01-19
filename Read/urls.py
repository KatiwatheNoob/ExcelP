from django.urls import path
from .views import index, fetch
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index)
]