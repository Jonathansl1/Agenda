from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from core.models import Contato
from django.db.models.functions import Concat
from django.db.models import Q, Value
from django.core.paginator import Paginator
from django.contrib.auth import login

def add_contato(request):
    if request.method != 'POST' :
        return render(request, 'core/add_contato.html')
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    descricao = request.POST['descricao']
    telefone = request.POST['telefone']
    imagem = request.FILES.get('imagem')

    if not nome or not sobrenome:
        return render(request, 'core/add_contato.html')
    salvarContato = Contato.objects.create(nome=nome,sobrenome=sobrenome, descricao=descricao, telefone=telefone, imagem=imagem)

    salvarContato.save()
    return render(request, 'core/add_contato.html')

@login_required
def listar_contato(request):
    contato = Contato.objects.all()
    return render(request, 'core/Listar_contato.html', {'contato':contato} )




def editarContato(request, id):
    contato =get_object_or_404(Contato, id=id)
    if request.method == 'POST' :
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        descricao = request.POST.get('descricao')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')


        contato.nome = nome
        contato.sobrenome = sobrenome
        contato.descricao = descricao
        contato.telefone = telefone
        contato.imagem = imagem
        contato.save()
        return redirect('Listar_contato')

    context = {
        'contato':contato
    }
    return render(request, 'core/editarContato.html', context)

def excluirContato(request, id):
    contato = Contato.objects.get(id=id)
    contato.delete()
    return redirect('Listar_contato')

def buscar_contato(request):
    termo = request.GET.get('termo')

    if not termo:
        messages.error(request, 'Campo não pode ser vazio!')
        return redirect('Listar_contato')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = (
        Contato.objects
        .annotate(nome_contato=campos)
        .filter(Q(nome_contato__icontains=termo))
    )

    paginator = Paginator(contatos, 6)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    if not contatos:
        messages.warning(request, 'Nenhum resultado encontrado.')

    context = {
        'contatos': contatos,
        'termo': termo,
    }

    return render(request, 'core/buscar_contato.html', context)


