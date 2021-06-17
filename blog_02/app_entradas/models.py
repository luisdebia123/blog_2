from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid


# Create your models here.

class Entradas(models.Model):
    titulo = models.CharField(max_length=300, default='DEFAULT VALUE')
    contenido = models.TextField(default='DEFAULT VALUE')
    img_destacada = models.ImageField(upload_to='fotos', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    class Meta:
        db_table = 'entradas'

    def __str__(self):
        return self.slug

def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return 

    id = str(uuid.uuid4())
    instance.slug = slugify( '{}-{}'.format(instance.titulo, id[:8]))

pre_save.connect(set_slug, sender=Entradas)