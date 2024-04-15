from django import forms

class Person(forms.Form):
  firstname = forms.CharField(label="Введите имя",max_length=50) 
  lastname  = forms.CharField(label="Введите фамилию", max_length = 100) 
