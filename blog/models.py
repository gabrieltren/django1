from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True, upload_to="blog")
    usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)