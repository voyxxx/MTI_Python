from django.urls import path, re_path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', views.about, kwargs={"name": "Vi", "age": 40}),
    re_path(r'^contact', views.contact),
]
