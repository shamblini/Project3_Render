from django.contrib import admin
from .models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe

# Edited admin to give a manager view look to it
admin.site.title = "Databases"
admin.site.site_header = "Manager View"
admin.site.index_title = "Databases"

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('time', 'products', 'cost')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'get_job')

    @admin.display(ordering='id', description='id')
    def get_job(self, obj):
        return Job.objects.get(id=obj.job_id).job_title

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'salary')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qty_stock', 'price', 'get_category')

    @admin.display(ordering='category', description='category')
    def get_category(self, obj):
        return Category.objects.get(id=obj.category_id).name

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'phone_number')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient_list', 'quantity')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Customer, CustomerAdmin)

# Register your models here.
# admin.site.register(Customer)
admin.site.register(Type)
# admin.site.register(Category)
# admin.site.register(Employee)
# admin.site.register(Job)
# admin.site.register(Product)
# admin.site.register(Transaction)
# admin.site.register(Recipe)