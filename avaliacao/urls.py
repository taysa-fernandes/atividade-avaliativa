"""
URL configuration for avaliacao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from core.views import *
urlpatterns = [
    path("alunos/", StudentView.as_view(), name="student"),
    path("edit-student/<int:pk>", EditStudentView.as_view(), name="edit_student"),
    path('criar-aluno/', CreateStudentView.as_view(), name='criar_aluno'),
    path('excluir-aluno/<int:pk>/', DeleteStudentView.as_view(), name='excluir_aluno'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='detalhes_aluno'),
]
    