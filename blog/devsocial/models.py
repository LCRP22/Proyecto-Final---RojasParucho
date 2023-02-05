from django.db import models
from django.conf import settings
from django.views import *
import datetime
# Create your models here

class post(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', default='imagen')
    fecha = models.DateField(default=datetime.date.today())
    
class comentario(models.Model):
    post= models.CharField(max_length=30, default="a")
    nombre = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    info = models.TextField(max_length=60)
    fecha = models.DateField(default=datetime.datetime.today())
