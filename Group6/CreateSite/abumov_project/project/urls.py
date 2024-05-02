from django.contrib import admin
from django.urls import path
from app.views import main_page, contactus, aboutus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('contacts/', contactus, name='contacts'),
    path('about_us/', aboutus, name='about_us'),
]