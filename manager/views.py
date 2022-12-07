from django.shortcuts import render, redirect
from django.template.defaulttags import register
from datetime import date, timedelta

from .analytics import salesReport, sellPairs, excessReport, restockReport

from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe, SalesReport

from DBModels.forms import ProductForm, CategoryForm, TransactionForm, EmployeeForm, JobForm, ModelForm, RecipeForm, CustomerForm, SalesReportForm, ExcessReportForm, SellPairsForm

# Create your views here.

# register = template.Library()

category_names = {}
for category in Category.objects.all():
    category_names[category.id] = category.name

job_names = {}
for job in Job.objects.all():
    job_names[job.id] = job.job_title


@register.filter
def get_category(dictionary: dict, key: int):
    return category_names.get(key)

@register.filter
def get_job(dictionary: dict, key: int):
    return job_names.get(key)

@register.filter
def format_recipe(list: 'list[str]'):
    ans = ""
    for i in range(len(list)):
        ans = ans + str(list[i])
        if i < len(list)-1:
            ans = ans + ", "
    return ans

@register.filter
def format_transaction(matrix: 'list[list[str]]'):
    ans = ""
    quants = {}
    for list in matrix:
        
        list_text = "["
        for i in range(len(list)):
            if list[i] != "-":
                list_text = list_text + list[i]
                if i < len(list)-1 and list[i + 1] != "-":
                    list_text = list_text + ", "
        list_text = list_text + "]"

        if list_text not in quants:
            quants[list_text] = 0
        quants[list_text] += 1
    
    for list in quants:
        ans += list + " x" + str(quants[list]) + '\n'
    
    return ans

def managerScreen(request):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    d2 = today + timedelta(days = 1)
    sr_result = salesReport(d1, d2)
    rs_result = restockReport()

    empty_vals = []
    for key in sr_result:
        if sr_result.get(key) == 0:
            empty_vals.append(key)
    
    for val in empty_vals:
        sr_result.pop(val)

    return render(request,"managerScreen.html", 
    {'sr_result' : sr_result,
     'rs_result' : rs_result,
     'date' : d1,})

def analytics(request):
    sr_form = SalesReportForm(request.POST or None)
    er_form = ExcessReportForm(request.POST or None)
    sp_form = SellPairsForm(request.POST or None)
    sr_result = {}
    er_result = {}
    rs_result = {}
    sp_result = {}

    if request.POST.get('form_type') == 'Load Sales' and sr_form.is_valid():
            sr_result = salesReport(sr_form.cleaned_data['s_time'], sr_form.cleaned_data['e_time'])

    if request.POST.get('form_type') == 'Load Excess' and er_form.is_valid():
        er_result = excessReport(er_form.cleaned_data['s_time'])

    if request.POST.get('form_type') == 'Load Pairs' and sp_form.is_valid():
        sp_result = sellPairs(sp_form.cleaned_data['s_time'], sp_form.cleaned_data['e_time'])

    rs_result = restockReport()

    return render(request,"analytics.html", 
    {'sr_form' : sr_form,
     'er_form' : er_form,
     'sp_form' : sp_form,
     'sr_result' : sr_result,
     'er_result' : er_result,
     'rs_result' : rs_result,
     'sp_result' : sp_result,})

# Product pages ------------------------------------------------------------------------------
def getProducts(request):
    context = {'products' : Product.objects.all()}
    return render(request,"products.html", context)

def addProduct(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-products')

    return render(request,"add.html", 
    {'form' : form,
     'type' : "Product",})

def showProduct(request, id):
    product = Product.objects.get(id = id)
    form = ProductForm(request.POST or None, instance=product)
    id = product.id

    if form.is_valid():
        form.save()
        return redirect('get-products')

    return render(request,"change.html", 
    {'item' : product,
     'form' : form,
     'id' : id,
     'type' : "Product"})

def deleteProduct(request, id):
    product = Product.objects.get(id = id).delete()
    return redirect('get-products')

# Category pages ------------------------------------------------------------------------------
def getCategories(request):
    context = {'categories' : Category.objects.all()}
    return render(request,"categories.html", context)

def showCategory(request, id):
    category = Category.objects.get(id = id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('get-categories')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Category"})

def addCategory(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-categories')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Category",
    'type' : "Category",})

def deleteCategory(request, id):
    product = Category.objects.get(id = id).delete()
    return redirect('get-categories')

# Transaction pages ------------------------------------------------------------------------------
def getTransactions(request):
    context = {'transactions' : Transaction.objects.all()}
    return render(request,"transactions.html", context)

def showTransaction(request, id):
    transaction = Transaction.objects.get(id = id)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('get-transactions')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Transaction"})

def addTransaction(request):
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-transactions')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Transaction",})

def deleteTransaction(request, id):
    product = Transaction.objects.get(id = id).delete()
    return redirect('get-transactions')

# Employee pages ------------------------------------------------------------------------------
def getEmployees(request):
    context = {'employees' : Employee.objects.all()}
    return render(request,"employees.html", context)

def showEmployee(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('get-employees')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Employee"})

def addEmployee(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-employees')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Employee",})

def deleteEmployee(request, id):
    product = Employee.objects.get(id = id).delete()
    return redirect('get-employees')

# Recipe pages ------------------------------------------------------------------------------
def getRecipes(request):
    context = {'recipes' : Recipe.objects.all()}
    return render(request,"recipes.html", context)

def showRecipe(request, id):
    recipe = Recipe.objects.get(id = id)
    form = RecipeForm(request.POST or None, instance=recipe)

    if form.is_valid():
        form.save()
        return redirect('get-recipes')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Recipe"})

def addRecipe(request):
    form = RecipeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-recipes')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Recipe",})

def deleteRecipe(request, id):
    product = Recipe.objects.get(id = id).delete()
    return redirect('get-recipes')

# Job pages ------------------------------------------------------------------------------
def getJobs(request):
    context = {'jobs' : Job.objects.all()}
    return render(request,"jobs.html", context)

def showJob(request, id):
    job = Job.objects.get(id = id)
    form = JobForm(request.POST or None, instance=job)

    if form.is_valid():
        form.save()
        return redirect('get-jobs')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Job"})

def addJob(request):
    form = JobForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('get-jobs')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Job",})

def deleteJob(request, id):
    product = Job.objects.get(id = id).delete()
    return redirect('get-jobs')

# Customer pages ------------------------------------------------------------------------------
def getCustomers(request):
    context = {'customers' : Customer.objects.all()}
    return render(request,"customers.html", context)

def showCustomer(request, id):
    customer = Customer.objects.get(id = id)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return redirect('get-customers')

    return render(request,"change.html", 
    {'item' : category,
     'form' : form,
     'id' : id,
     'type' : "Customer"})

def addCustomer(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('get-customers')

    return render(request,"add.html", 
    {'form' : form,
    'type' : "Customer",})

def deleteCustomer(request, id):
    product = Customer.objects.get(id = id).delete()
    return redirect('get-customers')
