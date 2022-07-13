from dataclasses import fields
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
        return Competicao.objects.filter(data__lte=timezone.now())

class CadastroView(generic.DetailView):
    model = Competicao
    template_name = 'cadastro.html'
    
    def cadastro(request, competicao_id):
        response = Competicao(pk=competicao_id)
        return render(request, 'cadastro.html', {'response': response})
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('index')