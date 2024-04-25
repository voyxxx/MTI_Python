"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app.views import *


store_url = [
    path('', index),
    path('catalog/', catalog),
    path('contacts/', contacts),
    path('catalog/<path:product_name>/', product),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include(store_url)),
    path('test/', test),
    path('json/', show_json),
    path('rand/', rand_product),  
    path('rand/<path:path_to_photo>/', img_product),  
]


# lesson 4
# store_url = [
#     path('', index_2),
#     path('catalog/', catalog),
#     path('catalog/<int:id>/', product),
#     path('contacts/', contacts)
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('rand/', rand),
#     path('store/', include(store_url)),
#     # path('hello/<str:name>/', greeting),
#     # re_path(r'^hello/(?P<name>\D+)/', greeting),
#     path('file/', file),
# ]