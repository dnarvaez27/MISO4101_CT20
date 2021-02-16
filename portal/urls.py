from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.redirect_to_auth, name="Home"),
    path('list/', views.list_object.as_view(), name="List_all"),
    url(r'adduser/$', views.add_user, name='addUser'),
]
