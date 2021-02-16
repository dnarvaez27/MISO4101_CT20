from django.urls import path
from portal import views

urlpatterns = [
    path('', views.list_object.as_view(), name="List_all"),
]
