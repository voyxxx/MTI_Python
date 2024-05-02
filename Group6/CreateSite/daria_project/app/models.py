from django.db import models
class Client(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=50)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15)
    email = models.EmailField(verbose_name='Email', max_length=50)
