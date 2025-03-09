from django.urls import path

from . import views

app_name = "sessions"

urlpatterns = [
    path("create_session", views.create_session, name="create_session"),
    path("read_session", views.read_session, name="read_session"),
    path("delete_session", views.delete_session, name="delete_session"),
    path("flush_session", views.flush_session, name="flush_session"),
]
