from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Participacion, UsuarioForm
from .serializers import ParticipacionSerializer
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class list_object(APIView):
    serializer_class = ParticipacionSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'participacion.html'

    def get(self, request):

        queryset = Participacion.objects.all()
        context = {'object': queryset}
        # print(context['object'][0])
        return Response(context)

def add_user(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adduser/')
    else:
        form = UsuarioForm()
    return render(request, 'user_form.html', {'form': form})


def redirect_to_auth(request):
    return redirect('auth/login')
