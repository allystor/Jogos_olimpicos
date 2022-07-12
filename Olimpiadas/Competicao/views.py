from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Competicao, Atleta


class IndexView(generic.ListView):
    template_name: str = 'index.html'
    
    def index(self, request):
        return render(request, 'index.html')
    
    def get_queryset(self):
        return Competicao.objects.filter(data_inicio__lte=timezone.now()).order_by('data_inicio')

class CadstroView(generic.CreateView):
    model = Competicao
    fields = ['nome', 'data_inicio', 'data_fim', 'descricao']
    template_name = 'cadastro.html'
    
    def cadastro(self, request):
        return render(request, 'cadastro.html')
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('index')