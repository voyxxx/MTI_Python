from django.db import models

# Create your models here.
class GoodsCategory(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.TextField()


class ProductManufacturer(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.TextField()