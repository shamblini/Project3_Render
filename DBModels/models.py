# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField as ArrayField

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.category_id) + ", " + self.name

    class Meta:
        managed = False
        db_table = 'category'


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    hired_date = models.DateField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        managed = False
        db_table = 'employee'


class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.job_title

    class Meta:
        managed = False
        db_table = 'job'

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
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


class Type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.type_id + ", " + self.type

    class Meta:
        managed = False
        db_table = 'type'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ", " + self.last_name

    class Meta:
        managed = False
        db_table = 'customer'

class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredient_list = ArrayField(models.CharField(max_length=100, blank=True, null=True)) 
    quantity = ArrayField(models.IntegerField(blank=True, null=True)) 

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'recipe'
 