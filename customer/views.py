from django.shortcuts import render
from .forms import buttonForm

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
    return render(request, 'Pizza_selection.html', {})

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
    return render(request, 'Cheese_selection.html', {})

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
    return render(request, 'Sauce_selection.html', {})

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
    return render(request, 'Toppings_selection.html', {})

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
    return render(request, 'Drizzle_selection.html', {})    

def Checkout(request):    
    return render(request, 'Checkout.html', {"currentOrder": currentOrder})        