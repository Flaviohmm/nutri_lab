from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')

        return HttpResponse(confirmar_senha)

def logar(request):
    pass
