from django.urls import path
from portal import views

urlpatterns = [
    path('', views.redirect_to_auth, name="Home"),
    path('list/', views.list_object.as_view(), name="List_all"),
]
