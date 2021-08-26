from django.urls import path
from . import views

app_name = "juegote"

urlpatterns = [
    path('', views.listar_preguntas, name='listar_preguntas'),
    # cuando en la url nos venga el string /preguntas/ va a ser manejada por la vista preguntas
    path('preguntas', views.preguntas),
    path("detalle_pregunta/<int:identificador>",
         views.detalle_pregunta, name="detalle_pregunta"),
    path('crear', views.crear_pregunta, name='crear_pregunta'),
    path("editar_pregunta/<int:identificador>", views.editar_pregunta),
    path('eliminar/<int:identificador>', views.eliminar_pregunta),
    path('confirmar_eliminacion/<int:identificador>',
         views.confirmar_eliminacion, name='confirmar_eliminacion'),
]
