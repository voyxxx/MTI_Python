from django.urls import path, include
from homework4 import views

product_patterns = [
    path("", views.index),
    path("page1", views.page1),
    path("page2", views.page2),
]

urlpatterns = [
    path("", views.index),
    path("pages/", include(product_patterns)),
]