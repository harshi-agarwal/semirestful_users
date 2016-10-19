from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def add_product(self,params):
        self.create(name=params['name'],description=params['description'],price=params['price'])


class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=255)
    price=models.IntegerField()

    objects=ProductManager()
