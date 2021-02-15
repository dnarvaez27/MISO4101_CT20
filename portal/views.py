from django.shortcuts import render
from .models import Participacion
from .serializers import ParticipacionSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

class list_object(APIView):
    serializer_class = ParticipacionSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'participacion.html'
    def get(self, request):

        queryset = Participacion.objects.all()
        context = {
            'object' : queryset
        }
        print(context['object'][0])
        return Response(context)