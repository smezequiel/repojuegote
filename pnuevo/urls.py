from django.contrib import admin
from django.urls import path, include
from usuario.views import registro, login, logout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('juegote', include('juegote.urls')),
    path('', include('usuario.urls')),
]
