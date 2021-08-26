from django.shortcuts import render, redirect
from .models import Categoria, Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import PreguntaForm
from django.contrib.auth.decorators import permission_required

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


def preguntas(request):
    # Usa el modelo Pregunta y se trae todos los modelos que tiene. Se trae todas las preguntas de la BD y las renderiza
    preguntas = Pregunta.objects.all()
    return render(request, 'juegote/preguntas.html', {"preguntas": preguntas})


def detalle_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juegote/detalle_pregunta.html', {"pregunta": pregunta})


@login_required(login_url='/login')
@permission_required('juegote.add_pregunta', login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juegote:preguntas')
    return render(request, 'juegote/crear_pregunta.html', {'form': form})


def editar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    if request.method == "POST":
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juegote:detalle_pregunta', identificador=item.id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render(request, 'juegote/editar_pregunta.html', {'form': form})


def eliminar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juegote/eliminar_pregunta.html', {"pregunta": pregunta})


def confirmar_eliminacion(request, identificador):
    Pregunta.objects.get(pk=identificador).delete()
    return redirect("/")
