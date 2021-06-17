from django.db import models
from django.utils import timezone


# Create your models here.

class Detalles_Blog(models.Model):
    detalles = models.CharField(max_length=6000, default='DEFAULT VALUE')
    logo = models.ImageField(upload_to='fotos', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'detalles_blog'