from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('results/<int:pk>', views.ResultsView.as_view(), name='results'),
    path('cadastrar/<int:competicao_id>', views.cadastrar, name='cadastrar'),
]