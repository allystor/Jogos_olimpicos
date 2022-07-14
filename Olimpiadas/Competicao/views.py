from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Competicao, Atleta


class IndexView(generic.ListView):
    template_name: str = 'index.html'
    
    def index(request):
        competicao = Competicao.objects.all()
        return render(request, 'index.html', {'competicao': competicao})
    
    def get_queryset(self):
        return Competicao.objects.filter(data__lte=timezone.now())

class CadastroView(generic.ListView):
    template_name = 'cadastro.html'
    
    def cadastro(request, competicao_id):
        competicao = get_object_or_404(Competicao,pk=competicao_id)
        return render(request, 'cadastro.html', {'competicao': competicao})
    
    def get_queryset(self):
        return Competicao.objects.filter(data__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Competicao
    template_name = 'results.html'

    def result(request, competicao_id):
        competicao = get_object_or_404(Competicao,pk=competicao_id)
        return render(request, 'results.html', {'competicao': competicao})

def cadastrar(request,competicao_id):
        competicao = get_object_or_404(Competicao, pk=competicao_id)
        try:
            selected_atleta = competicao.atleta_set.get(pk=request.POST['atleta'])
        except (KeyError, Atleta.DoesNotExist):
            return render(request,"cadastro.html",{
                'competicao': competicao,
                'error_message': "Voce não cadastrou nenhum atleta",
            })
        else:
            selected_atleta.cadastrar += 1
            selected_atleta.save()
            return HttpResponseRedirect(reverse('cadastrar', args=(competicao.id,)))
