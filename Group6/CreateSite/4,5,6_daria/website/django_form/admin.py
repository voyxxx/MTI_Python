from django.contrib import admin
from .models import *

class AdminProduct(admin.ModelAdmin):
  list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
  list_display = ['name']

  

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
