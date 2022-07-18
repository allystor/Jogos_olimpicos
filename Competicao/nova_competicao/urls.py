from django.urls import path

from . import views

urlpatterns = [
    path('', views.criar_competicao, name='criar_competicao'),
]
