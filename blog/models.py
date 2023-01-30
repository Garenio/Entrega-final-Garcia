from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenesreviews/')

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.fecha}"