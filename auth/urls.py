from django.urls import path
# from .views import signin, signout, login_user
from .views import *
urlpatterns = [
    # path('signin', signin, name='Sign In'),
    # path('signout', signout, name='Sign Out'),
    path('login', login_view, name='login'),
    path('loginUser/', login_user, name='loginUser'),
    path('logout/', logout_view, name='logout'),
    path('isLogged/', is_logged_view, name='isLogged'),
]
