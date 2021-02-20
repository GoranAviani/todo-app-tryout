from django.conf import settings
from django.urls import path

from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.list_lists, name="lists"),
    ]