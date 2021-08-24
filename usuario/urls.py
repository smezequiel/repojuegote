from django.contrib import admin
from django.urls import path
from usuario.views import registro, login, logout, home

urlpatterns = [
    path('registro', registro),
    path('login', login),
    path('logout', logout),
    path('', home)
]
