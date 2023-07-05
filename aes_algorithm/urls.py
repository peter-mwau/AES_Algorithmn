from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('homepage/', views.index, name="home"),
    path('logout/', views.logout_view, name='logout'),
]
