from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from phonenumber_field.modelfields import PhoneNumberField
# pip install django-phonenumber-field
# pip install django-phonenumbers

class Client(models.Model):
    name = models.CharField(verbose_name='ФИО клиента', max_length=30)
    number = PhoneNumberField(region='RU')
    email = models.EmailField(verbose_name='Электронная почта', unique=True)