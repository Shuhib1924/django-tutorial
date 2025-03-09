from django.urls import path

from . import views

app_name = "cookies"
urlpatterns = [
    path("set1", views.set1, name="set1"),
    path("get1", views.get1, name="get1"),
    path("delete1", views.delete1, name="delete1"),
]
