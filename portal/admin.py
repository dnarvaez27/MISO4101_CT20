from django import forms
from django.contrib import admin
from .models import Deportista, UsuarioRegistrado


# Register your models here.
@admin.register(Deportista)
class DeportistaForm(admin.ModelAdmin):
    pass


@admin.register(UsuarioRegistrado)
class UsuarioRegistrado(admin.ModelAdmin):
    pass
