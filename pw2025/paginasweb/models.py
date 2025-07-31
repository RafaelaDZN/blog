from django.db import models
from django.contrib.auth.models import User


TIPOS =(
    ("bom", "BOM"),
    ("legal", "LEGAL"),
    ("ruim", "Ruim"),
)

class Categoria(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Avaliacao(models.Model):
    tipo = models.CharField(max_length=100, choices=TIPOS)
    nota = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
