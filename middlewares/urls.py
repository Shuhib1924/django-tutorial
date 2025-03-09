from django.urls import path

from . import views

app_name = "middlewares"
urlpatterns = [
    path("", views.index, name="index"),
]
