from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .logic import signin as do_signup


# Create your views here.
@csrf_exempt
@api_view(["POST"])
def signin(request):
    username = request.data.get('username', '').lower()
    password = request.data.get('password', None)

    token = do_signup(request, username, password)

    return Response({'token': token}, status=status.HTTP_200_OK)
