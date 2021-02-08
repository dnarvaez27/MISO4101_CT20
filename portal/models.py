from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


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


class Lugar(models.Model):
    departamento = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    deportistaId = models.OneToOneField(Deportista, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lugares"


class Video(models.Model):
    url = models.URLField(verbose_name="Video", help_text="URL del video")
    participacion = models.OneToOneField(Participacion, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = ""


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    usuarioId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False)
    videoId = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comentarios"
