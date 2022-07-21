from multiprocessing import context
from django.shortcuts import render
from .forms import ClientForms
from .models import Competicao

def criar_competicao(request):
    if request.method == 'GET':
        form = ClientForms()
        context = {
            'form': form
        }
        return render(request, 'criar.html', context=context)
    else:
        form = ClientForms(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForms()
        context = {
            'form': form
        }
        return render(request, 'criar.html', context=context)

def ranking(request):
    context = Competicao.objects.all()
    ordenar = context.order_by('tempo_de_chegada_na_primeira_prova')
    return render(request, 'ranking.html', {'ordenar':ordenar})