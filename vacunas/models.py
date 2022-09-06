from django.db import models

# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    cant_dosis = models.IntegerField()

    def get_absolute_url(self):
        return reverse('index')