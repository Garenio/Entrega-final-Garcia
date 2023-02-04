from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=1000)
    cuerpo = models.CharField(max_length=1000, null=True)
    fecha_publicacion = models.DateField(null=True)
    autor = models.CharField(max_length=64)
    imagen = models.ImageField(null=True, blank=True, upload_to='imagenesreview')

    def __str__(self):
        return f"{self.titulo}"
