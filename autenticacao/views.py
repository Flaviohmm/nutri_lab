from django.http import HttpResponse
from django.shortcuts import redirect, render
from .utils import password_is_valid
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.messages import constants


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, password=senha, email=email, is_active=False)
            user.save()
            return redirect('/auth/login')
        except:
            return redirect('/auth/cadastro')


def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')