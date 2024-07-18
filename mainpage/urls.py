from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new-bin/", views.index, name="index"),
    path("my-bins/", views.index, name="index"),
    path("account/", views.index, name="index"),
    path("new-bin/add/", views.add, name="add"),
]
