from django.db import models
from django.utils import timezone


# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=1300, default='DEFAULT VALUE')
    img_destacada = models.ImageField(upload_to='fotos', null=True)
    web = models.CharField(max_length=1300, default='DEFAULT VALUE')
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'usuarios'
