from .models import Participacion
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


def redirect_to_auth(request):
    return redirect('auth/login')
