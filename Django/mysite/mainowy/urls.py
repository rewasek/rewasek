from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="index"),
    path("v2/", views.v2, name="index"),
    path("v2/", views.v2, name="index"),
]
