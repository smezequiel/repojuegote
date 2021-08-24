from django.contrib import admin
from django.urls import path, include
from usuario.views import registro, login, logout, home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('juegote', include('juegote.urls')),
    path('', include('usuario.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
