from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()