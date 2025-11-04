from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    if request.method != "POST":
        return render(request, "acounts/login.html")
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)
    if user is not None:
            login(request, user)
            messages.success(request, 'Sucesso!')
            return redirect('Listar_contato')
    messages.error(request, 'Email ou senha incorreta')
    return redirect('Listar_contato')