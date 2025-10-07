from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=10)
    descricao = models.TextField(max_length=255)
    telefone = models.CharField(max_length=20)  # Alterado de IntegerField para CharField
    imagem = models.ImageField(upload_to='core_image/%Y/%m', blank=True, null=True)
    ########
