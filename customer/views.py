from django.shortcuts import render

# Create your views here.
def customerScreen(request):
    return render(request, 'Pizza_selection.html', {})

def Cheese_selection(request):    
    return render(request, 'Cheese_selection.html', {})

def Sauce_selection(request):    
    return render(request, 'Sauce_selection.html', {})

def Toppings_selection(request):    
    return render(request, 'Toppings_selection.html', {})

def Drizzle_selection(request):    
    return render(request, 'Drizzle_selection.html', {})    

def Checkout(request):    
    return render(request, 'Checkout.html', {})        