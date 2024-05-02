from django import forms
from .models import Product

class ClientForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=2, label='Введите имя:')
    phone = forms.CharField(max_length=50, min_length=2, label='Введите телефон:')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'