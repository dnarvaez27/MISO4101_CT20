from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UsuarioForm


def add_user(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/adduser/')
    else:
        form = UsuarioForm()
    return render(request, 'user_form.html', {'form': form})
# Create your views here.
