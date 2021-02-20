from django.conf import settings
from django.urls import path

from todo import views


urlpatterns = [
    path("", views.list_lists, name="lists"),
    ]