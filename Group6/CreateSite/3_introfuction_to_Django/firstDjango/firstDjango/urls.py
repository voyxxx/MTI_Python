from django.urls import path
from homework3 import views

urlpatterns = [
    path("", views.index),
    path("game", views.game),
]
