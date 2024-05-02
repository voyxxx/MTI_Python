from django.contrib import admin
from .models import Product, Consumer

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'old_price')

class AdminConsumer(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment', 'is_agree')

admin.site.register(Product, AdminProduct)
admin.site.register(Consumer, AdminConsumer)
