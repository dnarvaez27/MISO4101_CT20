from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Deportista(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True, verbose_name='Usuario')
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    peso = models.FloatField(validators=[MinValueValidator(0.0)], help_text='Peso del Deportista')
    estatura = models.FloatField(validators=[MinValueValidator(0.0)], help_text='Estatura del Deportista')
    entrenador = models.CharField(max_length=128, help_text='Entrenador del Deportista')
    imagen = models.URLField(verbose_name='Foto', help_text='URL Foto de Perfil')

    class Meta:
        verbose_name_plural = 'Deportistas'


class UsuarioRegistrado(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True, verbose_name='Usuario')
    email = models.EmailField(help_text='Correo electrónico del Usuario')

    class Meta:
        verbose_name_plural = 'Usuarios Registrados'
