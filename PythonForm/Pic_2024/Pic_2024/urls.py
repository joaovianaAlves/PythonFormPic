from django.urls import path
from app_cad_pic import views

urlpatterns = [
    path("", views.home, name="home"),
    path("alunos/", views.alunos, name="listagem_alunos"),
]
