from django.shortcuts import render

def _add_contato(request):
    render(request, 'core/add_contato.html')