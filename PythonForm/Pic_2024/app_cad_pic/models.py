from django.db import models


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    turma = models.CharField(max_length=2)
    pic = models.TextField(max_length=255)
