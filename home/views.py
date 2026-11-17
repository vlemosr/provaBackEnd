from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
# 1. READ & CREATE (Lista todas e recebe novas via POST)
def listar_tarefas(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        if titulo:
            Tarefa.objects.create(titulo=titulo)
        return redirect("listar_tarefas")
    tarefas = Tarefa.objects.all()
    return render(request, "home/tarefas.html", {"tarefas": tarefas})
# 2. UPDATE (Edita uma tarefa existente)
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == "POST":
        tarefa.titulo = request.POST.get("titulo")
        tarefa.save()
        return redirect("listar_tarefas")
    return render(request, "home/editar.html", {"tarefa": tarefa})
# 3. DELETE (Remove uma tarefa)
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("listar_tarefas")

