from django.db import models

class product(models.Model):
  title = models.CharField(max_length=30, unique=True)
  description = models.TextField()
  img = models.CharField(max_length=100)
  oldPrice = models.IntegerField()
  price = models.IntegerField()