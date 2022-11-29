from django.shortcuts import render
from .forms import buttonForm
from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe


currentOrder = []
from django.shortcuts import redirect

# Create your views here.
def customerScreen(request):
    if request.method == 'POST':
        form = buttonForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            currentOrder.append(val) 
            print(currentOrder)
            return redirect('Cheese_selection/')
    else:
        form = buttonForm()
    
    orderNames = []
    orders = Product.objects.filter(category_id=2) #Get orders
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    return render(request, 'Pizza_selection.html', {"orderNames":orderNames})

def Cheese_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                currentOrder.append(val) 
                print(currentOrder)
                return redirect('Sauce_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=3) #Get Cheese
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    return render(request, 'Cheese_selection.html', {"orderNames":orderNames})

def Sauce_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                currentOrder.append(val) 
                print(currentOrder)
                return redirect('Toppings_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=7) #Get sauce
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    return render(request, 'Sauce_selection.html', {"orderNames":orderNames})

def Toppings_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                currentOrder.append(val) 
                print(currentOrder)
                return redirect('Drizzle_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=6) #Get meat topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    orderNames2 = []
    orders = Product.objects.filter(category_id=9) #Get meat topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames2.append(name)
        
    return render(request, 'Toppings_selection.html', {"orderNames":orderNames, "orderNames2":orderNames2})

def Drizzle_selection(request):  
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                currentOrder.append(val) 
                print(currentOrder)
                return redirect('Checkout/')
    else:
        form = buttonForm()  
        
    orderNames = []
    orders = Product.objects.filter(category_id=5) #Drizzle topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    return render(request, 'Drizzle_selection.html', {"orderNames":orderNames})    

def Checkout(request):    
    return render(request, 'Checkout.html', {"currentOrder": currentOrder})        