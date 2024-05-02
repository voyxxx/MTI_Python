from django.db import models

class Category(models.Model):
  class Meta:
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  name = models.CharField(max_length=50, verbose_name='название')
  def __str__(self):
    return self.name


class Product(models.Model):
  class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
  name = models.CharField(max_length=50, verbose_name='название')
  price = models.IntegerField(verbose_name='цена')
  path = models.CharField(max_length=150, verbose_name='путь к изображению')
  link_name = models.CharField(max_length=50, verbose_name='адрес ссылки')
  

  def __str__(self):
    return self.name
