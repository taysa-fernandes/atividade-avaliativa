from django.db import models

class cidade(models.Model):
    nome = models.CharField(max_length=255)
    sigla_estado = models.CharField(max_length=2)
    def __str__(self):
        return self.nome

class curso(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
    
class aluno(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email =  models.EmailField(max_length= 255)
    data_de_nascimento = models.DateField()
    cidade = models.ForeignKey(cidade,on_delete=models.CASCADE,default="não definido")
    curso = models.ForeignKey(curso,on_delete=models.CASCADE,default="não definido")
    
    def __str__(self):
        return self.nome
    
