from django.urls import path

from . import views

app_name = "middlewares"
urlpatterns = [
    path("", views.index, name="index"),
    path("exception/", views.exception, name="exception"),
    path("templates/", views.templates, name="templates"),
]
