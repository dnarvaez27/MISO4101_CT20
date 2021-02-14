from django.contrib.auth import get_user_model, authenticate, login
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=get_user_model())
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        # Creates the auth token for the user
        Token.objects.create(user=instance)


def signin(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        user.save()
        token = Token.objects.get(user=user)
        return user, token.key
    else:
        raise Exception('Error on credentials')
