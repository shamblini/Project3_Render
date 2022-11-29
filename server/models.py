from django.db import models
from django.contrib.postgres.fields import ArrayField as ArrayField

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qty_stock = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'product'

class Transaction(models.Model):
    # id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    products = ArrayField(ArrayField(models.CharField(max_length=50, blank=True, null=True)))
    time = models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    # def __str__(self):
    #     return str(self.time) + str(self.products)

    class Meta:
        managed = False
        db_table = 'transaction'
        ordering = ('-time',)

class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredient_list = ArrayField(models.CharField(max_length=100, blank=True, null=True)) 
    quantity = ArrayField(models.IntegerField(blank=True, null=True)) 

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'recipe'
 