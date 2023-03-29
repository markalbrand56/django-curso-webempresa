from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User  # Esto contiene todos los usuarios registrados en el sitio web


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de adición')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # On delete. Cuando se borra el usuario qué es lo que hace Django con lo que está relacionado
    categories = models.ManyToManyField(Category, verbose_name="Categorías")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de adición')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ["-created"]

    def __str__(self):
        return self.title
