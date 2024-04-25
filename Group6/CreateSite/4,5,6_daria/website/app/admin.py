from django.contrib import admin
from .models import *

class AdminProduct(admin.ModelAdmin):
  list_display = ['name', 'price', 'category']

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
