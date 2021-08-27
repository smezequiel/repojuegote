from django.shortcuts import render, redirect
from .models import Categoria, Pregunta, Respuesta, Partida
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import PreguntaForm
from .forms import RespuestaForm
from django.contrib.auth.decorators import permission_required

# Create your views here.


@login_required(login_url='/login')
def listar_preguntas(request):
    if request.method == "POST":
        resultado = 0
        for i in range(1, 8):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user,
                               fecha=datetime.now, resultado=resultado)
        return redirect("/")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by(
            '?')[:10]  # Cuantas preguntas se van a mostrar
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta=item.id)
            categoria = Categoria.objects.get(pk=item.id_categoria.id)
            # {pregunta: {opciones: [opcion1, opcion2, opcion] categoria: categoria}
            data[item.pregunta] = {
                "opciones": respuestas, "categoria": categoria}

        return render(request, 'juegote/listar_preguntas.html', {"preguntas": preguntas, "data": data})


@login_required(login_url='/login')
# la expresion correcta de view y eso lo vemos en el admin de la app
@permission_required('juegote.view_pregunta', login_url='/login')
def preguntas(request):
    # Usa el modelo Pregunta y se trae todos los modelos que tiene. Se trae todas las preguntas de la BD y las renderiza
    preguntas = Pregunta.objects.all()
    return render(request, 'juegote/preguntas.html', {"preguntas": preguntas})


@login_required(login_url='/login')
# la expresion correcta de view y eso lo vemos en el admin de la app
@permission_required('juegote.view_pregunta', login_url='/login')
def detalle_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juegote/detalle_pregunta.html', {"pregunta": pregunta})


@login_required(login_url='/login')
# la expresion correcta de add y eso lo vemos en el admin de la app
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


@login_required(login_url='/login')
# la expresion correcta de edit y eso lo vemos en el admin de la app
@permission_required('juegote.edit_pregunta', login_url='/login')
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


@login_required(login_url='/login')
# la expresion correcta de delete y eso lo vemos en el admin de la app
@permission_required('juegote.delete_pregunta', login_url='/login')
def eliminar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juegote/eliminar_pregunta.html', {"pregunta": pregunta})


def confirmar_eliminacion(request, identificador):
    Pregunta.objects.get(pk=identificador).delete()
    return redirect("/")


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


@login_required(login_url='/login')
# la expresion correcta de view y eso lo vemos en el admin de la app
@permission_required('juegote.view_respuesta', login_url='/login')
def listar_respuestas(request):
    # Usa el modelo Pregunta y se trae todos los modelos que tiene. Se trae todas las preguntas de la BD y las renderiza
    respuestas = Respuesta.objects.all()
    return render(request, 'juegote/listar_respuestas.html', {"respuestas": respuestas})


@login_required(login_url='/login')
# la expresion correcta de view y eso lo vemos en el admin de la app
@permission_required('juegote.view_respuesta', login_url='/login')
def detalle_respuesta(request, identificador):
    respuesta = Respuesta.objects.get(pk=identificador)
    return render(request, 'juegote/detalle_respuesta.html', {"respuesta": respuesta})


@login_required(login_url='/login')
# la expresion correcta de add y eso lo vemos en el admin de la app
@permission_required('juegote.add_respuesta', login_url='/login')
def crear_respuesta(request):
    form = RespuestaForm()
    if request.method == "POST":
        # Lo vamos a crear de la misma forma que creamos en forms.py
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()  # A diferencia del anterior, el commit era False porque tambien le ibamos a agregar fecha de creacion y autor, en este caso no tenemos ninguno de los dos asi que podemos ponerle que guarde en la BD
            return redirect('juegote:listar_respuestas')
    return render(request, 'juegote/crear_respuesta.html', {'form': form})


@login_required(login_url='/login')
# la expresion correcta de change y eso lo vemos en el admin de la app
@permission_required('juegote.change_respuesta', login_url='/login')
def editar_repuesta(request, identificador):
    pregunta = Respuesta.objects.get(pk=identificador)
    if request.method == "POST":
        # Lo vamos a crear de la misma forma que creamos en forms.py
        form = RespuestaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('juegote:detalle_respuesta', identificador=item.id)
    else:
        # Tambien la vamos a crear en forms.py
        form = RespuestaForm(instance=pregunta)
    return render(request, 'juegote/editar_respuesta.html', {'form': form})


@login_required(login_url='/login')
# la expresion correcta de delete y eso lo vemos en el admin de la app
@permission_required('juegote.delete_respuesta', login_url='/login')
def eliminar_respuesta(request, identificador):
    pregunta = Respuesta.objects.get(pk=identificador)
    return render(request, 'juegote/eliminar_respuesta.html', {"pregunta": pregunta})


@login_required(login_url='/login')
# la expresion correcta de delete y eso lo vemos en el admin de la app
@permission_required('juegote.delete_respuesta', login_url='/login')
def confirmar_resp_eliminacion(request, identificador):
    Respuesta.objects.get(pk=identificador).delete()
    return redirect("juegote:listar_respuestas")
