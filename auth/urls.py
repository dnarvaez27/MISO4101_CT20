from django.urls import path
from .views import signin, signout, login_user

urlpatterns = [
    path('signin', signin, name='Sign In'),
    path('signout', signout, name='Sign Out'),
    path('login', login_user, name='Log in'),
]
