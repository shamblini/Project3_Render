from django.contrib import admin
from .models import P3Category, P3Employee, P3Job, P3Product, P3Transaction, P3Type, P3User, Recipe

# Edited admin to give a manager view look to it
admin.site.title = "Databases"
admin.site.site_header = "Manager View"
admin.site.index_title = "Databases"

# Register your models here.
admin.site.register(P3User)
admin.site.register(P3Type)
admin.site.register(P3Category)
admin.site.register(P3Employee)
admin.site.register(P3Job)
admin.site.register(P3Product)
admin.site.register(P3Transaction)
admin.site.register(Recipe)
