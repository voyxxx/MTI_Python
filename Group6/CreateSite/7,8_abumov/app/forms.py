from django import forms
from .models import Product, Catalog

class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'brand', 'price']

class StudentForm(forms.Form):
  firstname = forms.CharField(label='Enter first name', max_length=50)
  lastname = forms.CharField(label='Enter last name', max_length=100)
