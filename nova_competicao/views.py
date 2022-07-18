from multiprocessing import context
from django.shortcuts import render
from .forms import ClientForms

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