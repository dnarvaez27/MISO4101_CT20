from django.urls import path
from django.conf.urls import url, include
from portal import views

urlpatterns = [
    path('', views.list_object.as_view(), name="List_all"),
 ]