# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    manager = models.ForeignKey('Manager', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    pay = models.FloatField(blank=True, null=True)
    on_shift = models.TextField(blank=True, null=True)  # This field type is a guess.
    hours_worked = models.FloatField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Inventory(models.Model):
    ingredient = models.TextField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    unit = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    item_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Manager(models.Model):
    name = models.TextField(blank=True, null=True)
    pay = models.FloatField(blank=True, null=True)
    on_shift = models.TextField(blank=True, null=True)  # This field type is a guess.
    hours_worked = models.FloatField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Recipe(models.Model):
    name = models.TextField(blank=True, null=True)
    ingredient_list = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'recipe'
# Unable to inspect table 't'
# The error was: permission denied for table t


class Teammembers(models.Model):
    student_name = models.TextField(primary_key=True)
    section = models.IntegerField(blank=True, null=True)
    favorite_movie = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teammembers'


class Transactions(models.Model):
    manager = models.ForeignKey(Manager, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    item = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'transactions'
