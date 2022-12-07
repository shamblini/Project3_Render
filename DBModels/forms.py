from django import forms
from django.forms import ModelForm

from .models import Product, Transaction, Employee, Category, Customer, Recipe, Job, SalesReport, ExcessReport, SellPairs

class ProductForm(ModelForm):
    class Meta:

            categories = Category.objects.all()
            id_list = []
            for category in categories:
                id_list.append((category.id, category.name))

            model = Product

            fields = ('name', 'qty_stock', 'price', 'category_id', 'description')

            labels = {
                # 'product_id': 'Product Id:',
                'name': 'Name:',
                'qty_stock': 'Qty Stock:',
                'price': 'Price:',
                'category_id': 'Category:',
                'description': 'Description:',
            }

            widgets = {
                # 'product_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product ID'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'qty_stock': forms.NumberInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                # 'category_id': forms.NumberInput(attrs={'class': 'form-control'}),
                'category_id': forms.Select(attrs={'class': 'form-control'}, choices=id_list),
                'description': forms.Textarea(attrs={'class': 'form-control', 'rows':15,'cols':150}),
            }

class CategoryForm(ModelForm):
    class Meta:
            model = Category

            fields = ('name', 'description',)

            labels = {
                # 'id': 'ID:',
                'name': 'Name:',
                'description': 'Description:',
            }

            widgets = {
                # 'id': forms.NumberInput(attrs={'class': 'form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control', 'rows':15,'cols':120}),
            }

class TransactionForm(ModelForm):
    class Meta:
            model = Transaction

            fields = ('products', 'time', 'type', 'cost')

            labels = {
                # 'id': 'ID:',
                'products': 'Items:',
                'time': 'Time:',
                'type': 'Payment Type:',
                'cost': 'Cost:',
            }

            widgets = {
                # 'id': forms.NumberInput(attrs={'class': 'form-control'}),
                'products': forms.Textarea(attrs={'class': 'form-control', 'rows':15,'cols':120}),
                'time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
                'type': forms.NumberInput(attrs={'class': 'form-control'}),
                'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            }

class CustomerForm(ModelForm):
    class Meta:
            model = Customer

            fields = ('first_name', 'last_name', 'username', 'type_id', 'phone_number')

            labels = {
                'first_name': 'First Name:',
                'last_name': 'Last Name:',
                'username': 'Username:',
                'type_id': 'Type ID:',
                'phone_number': 'Phone Number:',
            }

            widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'type_id': forms.NumberInput(attrs={'class': 'form-control'}),
                'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            }

class EmployeeForm(ModelForm):
    class Meta:

        jobs = Job.objects.all()
        id_list = []
        for job in jobs:
            id_list.append((job.id, job.job_title))

            model = Employee

            fields = ('first_name', 'last_name', 'email', 'phone_number', 'job_id', 'hired_date', 'location_id')

            labels = {
                'first_name': 'First Name:',
                'last_name': 'Last Name:',
                'email': 'Email:',
                'phone_number': 'Phone Number:',
                'job_id': 'Job:',
                'hired_date': 'Hired Date:',
                'location_id': 'Location ID:',
            }

            widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
                'job_id': forms.Select(attrs={'class': 'form-control'}, choices=id_list),
                'hired_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
                'location_id': forms.NumberInput(attrs={'class': 'form-control'}),
            }

class JobForm(ModelForm):
    class Meta:
            model = Job

            fields = ('job_title', 'salary',)

            labels = {
                'job_title': 'Job Title:',
                'salary': 'Salary:',
            }

            widgets = {
                'job_title': forms.TextInput(attrs={'class': 'form-control'}),
                'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            }

class RecipeForm(ModelForm):
    class Meta:
            model = Recipe

            fields = ('name', 'ingredient_list', 'quantity',)

            labels = {
                'name': 'Name:',
                'ingredient_list': 'Ingredients:',
                'quantity': 'Quantities:',
            }

            widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'ingredient_list': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item_1, Item_2, ...'}),
                'quantity': forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Quantity_1, Quantity_2, ...'}),
            }

class SalesReportForm(ModelForm):
    class Meta:
        model = SalesReport

        fields = ('s_time', 'e_time',)

        labels = {
                's_time': 'Start Time:',
                'e_time': 'End Time:',
            }

        widgets = {
                's_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
                'e_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            }

class ExcessReportForm(ModelForm):
    class Meta:
        model = ExcessReport

        fields = ('s_time',)

        labels = {
                's_time': 'Start Time:',
            }

        widgets = {
                's_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            }

class SellPairsForm(ModelForm):
    class Meta:
        model = SellPairs

        fields = ('s_time', 'e_time',)

        labels = {
                's_time': 'Start Time:',
                'e_time': 'End Time:',
            }

        widgets = {
                's_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
                'e_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            }