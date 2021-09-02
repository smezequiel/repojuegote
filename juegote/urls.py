from django.urls import path
from . import views

app_name = "juegote"

urlpatterns = [
    path('<int:identificador>', views.listar_preguntas, name='listar_preguntas'),
    # cuando en la url nos venga el string /preguntas/ va a ser manejada por la vista preguntas
    path('preguntas', views.preguntas, name='preguntas'),
    path("detalle_pregunta/<int:identificador>",
         views.detalle_pregunta, name="detalle_pregunta"),
    path('crear', views.crear_pregunta, name='crear_pregunta'),
    path("editar_pregunta/<int:identificador>",
         views.editar_pregunta, name="editar_pregunta"),
    path('eliminar/<int:identificador>',
         views.eliminar_pregunta, name='eliminar'),
    path('confirmar_eliminacion/<int:identificador>',
         views.confirmar_eliminacion, name='confirmar_eliminacion'),

    path('listar_respuestas', views.listar_respuestas, name="respuestas"),
    path("detalle_respuesta/<int:identificador>",
         views.detalle_respuesta, name="detalle_respuesta"),
    path('crear_respuesta', views.crear_respuesta, name='crear_respuesta'),
    path("editar_respuesta/<int:identificador>",
         views.editar_repuesta, name="editar_respuesta"),
    path('eliminar_respuesta/<int:identificador>',
         views.eliminar_respuesta, name='eliminar_respuesta'),
    path('confirmar_resp_eliminacion/<int:identificador>',
         views.confirmar_resp_eliminacion, name='confirmar_resp_eliminacion'),

    path('categorias', views.elegir_categorias, name='categorias'),
    path('preguntas_categorias', views.preguntas_categorias,
         name='preguntas_categorias'),
    path('categoria/<int:id>', views.categoria_page, name='categoria'),
    path('', views.elegir_categorias, name='categorias'),

]
