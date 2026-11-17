from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
]
