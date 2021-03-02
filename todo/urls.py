from django.conf import settings
from django.urls import path

from todo import views

app_name = "todo"


urlpatterns = [
    path("", views.list_lists, name="lists"),
    path("mine/", views.list_detail, {"list_slug": "mine"}, name="mine"),
    path(
        "<int:list_id>/<str:list_slug>/completed/",
        views.list_detail,
        {"view_completed": True},
        name="list_detail_completed",
    ),
    path("<int:list_id>/<str:list_slug>/", views.list_detail, name="list_detail"),
    ]