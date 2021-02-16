from django.urls import path
from .views import signin, signout, login_view

urlpatterns = [
    path('signin', signin, name='Sign In'),
    path('signout', signout, name='Sign Out'),
    path('login/', login_view, name='login'),
]
