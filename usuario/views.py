from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "usuario/login.html", {'form': form})


def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "usuario/registro.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')


def home(request):
    permisos = request.user.get_all_permissions()
    return render(request, 'usuario/home.html', {"permisos": "permisos"})
