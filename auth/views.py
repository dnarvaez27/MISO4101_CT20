from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .logic import signin as do_signup, signout as do_signout
from .serializers import UserSerializer


@api_view(["POST"])
def signin(request):
    username = request.data.get('username', '').lower()
    password = request.data.get('password', None)

    try:
        user, token = do_signup(request, username, password)
        return Response({
            'token': token,
            'data': UserSerializer(user).data,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)


def login_user(request):
    return render(request, 'portal/login.html')


@api_view(["POST"])
def signout(request):
    do_signout(request, user=request.user)
    return Response(status=status.HTTP_200_OK)
