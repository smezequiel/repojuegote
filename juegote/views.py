from django.shortcuts import render, redirect
from .models import Categoria, Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login')
def listar_preguntas(request):
    if request.method == "POST":
        resultado = 0
        for i in range(1, 4):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user,
                               fecha=datetime.now, resultado=resultado)
        return redirect("/")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by(
            '?')[:3]  # Cuantas preguntas se van a mostrar
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            categoria = Categoria.objects.get(pk=item.id_categoria.id)
            # {pregunta: {opciones: [opcion1, opcion2, opcion] categoria: categoria}
            data[item.pregunta] = {
                "opciones": respuestas, "categoria": categoria}

        return render(request, 'juegote/listar_preguntas.html', {"preguntas": preguntas, "data": data})
