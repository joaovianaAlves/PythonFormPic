from django.shortcuts import render
from .models import Aluno


def home(request):
    return render(request, "alunos/home.html")


def alunos(request):
    if request.method == "POST":
        if "delete_all" in request.POST:
            Aluno.objects.all().delete()
        else:
            nome = request.POST.get("nomeCompleto")
            turma = request.POST.get("turma")
            pic = request.POST.get("pic")

            if not Aluno.objects.filter(nome=nome).exists():
                Aluno.objects.create(nome=nome, turma=turma, pic=pic)

    alunos = {"alunos": Aluno.objects.all()}
    return render(request, "alunos/alunos.html", alunos)
