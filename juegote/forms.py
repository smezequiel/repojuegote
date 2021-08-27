from django import forms
from .models import Pregunta, Respuesta


class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('pregunta', 'id_categoria')


class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Respuesta
        # Vamos a models y vemos que campos (fields) tenemos disponibles
        fields = ('id_pregunta', 'opcion', 'puntaje')
