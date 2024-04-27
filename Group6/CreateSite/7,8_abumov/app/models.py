from django.db import models
# from django.apps import Catalog

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Catalog(models.Model):
  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  name = models.CharField(max_length=50, verbose_name='название')
  def __str__(self):
    return self.name


class Product(models.Model):
    title = models.CharField(max_length=30, default='Введите название товара',
                             verbose_name='Название товара', unique=True)
    brand = models.ForeignKey(Catalog, on_delete=models.CASCADE, default=1, verbose_name='Производитель')
    price = models.IntegerField(default=0, verbose_name='Цена')
    abount = models.IntegerField(default=0, verbose_name='Остаток товара на складе')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}{self.brand}'

