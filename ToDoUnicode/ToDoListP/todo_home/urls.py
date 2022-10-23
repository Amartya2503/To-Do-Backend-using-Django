from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name= 'test'),
    path('display/', views.index, name = 'dispaly')
]
