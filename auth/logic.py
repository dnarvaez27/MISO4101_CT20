from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


def signin(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        user.save()
        token = Token.objects.get(user=user)
        return token.key
    else:
        raise Exception('Error on credentials')
