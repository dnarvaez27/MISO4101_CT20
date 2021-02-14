from django.urls import path
from .views import signin, signout

urlpatterns = [
    path('signin', signin, name='Sign In'),
    path('signout', signout, name='Sign Out'),
]
