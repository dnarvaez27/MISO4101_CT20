import json

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .logic import signin as do_signup, signout as do_signout
from .serializers import UserSerializer

#
# @api_view(["POST"])
# def signin(request):
#     username = request.data.get('username', '').lower()
#     password = request.data.get('password', None)
#
#     try:
#         user, token = do_signup(request, username, password)
#         return Response({
#             'token': token,
#             'data': UserSerializer(user).data,
#         }, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
#
#
#
#
#
# @api_view(["POST"])
# def signout(request):
#     do_signout(request, user=request.user)
#     return Response(status=status.HTTP_200_OK)


# @csrf_exempt
# def add_user_view(request):
#     if request.method == 'POST':
#         jsonUser = json.loads(request.body)
#         username = jsonUser['username']
#         first_name = jsonUser['first_name']
#         last_name = jsonUser['last_name']
#         password = jsonUser['password']
#         email = jsonUser['email']
#
#         user_model = User.objects.create_user(username=username, password=password)
#         user_model.first_name = first_name
#         user_model.last_name = last_name
#         user_model.email = email
#         user_model.save()
#     return HttpResponse(serializers.serialize("json", [user_model]))


# @csrf_exempt
# def add_user(request):
#     return render(request, "gallery/register.html")


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o contraseña incorrectos'

    return JsonResponse({"message": message})


@csrf_exempt
def login_user(request):
    return render(request, "portal/login.html")


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message": 'ok'})


@csrf_exempt
def is_logged_view(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        message = 'ok'
    else:
        message = 'no'
    return JsonResponse({"message": message})
