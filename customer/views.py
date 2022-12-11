from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import buttonForm
from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe
from django.shortcuts import redirect
import SQLFunctions
from django.contrib.auth.decorators import login_required

currentOrder = []
fullOrder = []
orderDict = {'editOrderNum':-1, 'numberToppings':-1, 'popup':"none", "otherCheckoutButton":""}
orderProg = {"order": 1, "crust": -1, "cheese": -1, "sauce": -1, "topping": -1, "drizzle": -1, "checkout": -1}


def customerMakeTransaction():
    createTransactionFullList = []
    subOrderList = []
    # Make it work for createTransaction
    for order in fullOrder:
        for quantity in range(order[0]):
            for item in order[1]:
                fixedItem = item.replace(" ", "_").lower()
                subOrderList.append(fixedItem)
            createTransactionFullList.append(subOrderList.copy())
            subOrderList.clear()
            
    for i in createTransactionFullList:
        print(i)
    SQLFunctions.createTransaction(createTransactionFullList)
    return

def outOfOrder():
    orderProg["order"] = 1;
    orderProg["crust"] = -1;
    orderProg["cheese"] = -1;
    orderProg["sauce"] = -1;
    orderProg["topping"] = -1;
    orderProg["drizzle"] = -1;
    orderProg["checkout"] = -1;
    orderDict["popup"] = "none";
    orderDict["otherCheckoutButton"] = ""
    currentOrder.clear()
    fullOrder.clear()

# Create your views here.
@login_required
def customerScreen(request):
    if request.method == 'POST':
        form = buttonForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            currentOrder.append(val) 
            
            if orderProg["order"] != 1:
                outOfOrder();
                return redirect('/login')
                    
            # Order based logic 
            if val=="One topping":
                orderProg["order"] = -1;
                orderProg["crust"] = 1;
                orderDict['numberToppings'] = 1
                return redirect('Crust_selection/')

            elif val=="Four topping":
                orderProg["order"] = -1;
                orderProg["crust"] = 1;
                orderDict['numberToppings'] = 4
                return redirect('Crust_selection/')
            
            elif val=="Cheese pizza":
                orderProg["order"] = -1;
                orderProg["crust"] = 1;
                orderDict['numberToppings'] = 0
                return redirect('Crust_selection/')
            
            elif val=="Pepperoni pizza":
                orderProg["order"] = -1;
                orderProg["crust"] = 1;
                orderDict['numberToppings'] = 0
                return redirect('Crust_selection/')
            
            elif val=="Checkout":
                orderProg["order"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            
            else:
                orderProg["order"] = -1;
                orderProg["checkout"] = 1;
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/') 
            
    else:
        form = buttonForm()
    
    currentOrder.clear() #Clear my order since a new one is starting
    orderNames = []
    orders = Product.objects.filter(category_id=2) #Get orders
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
    
    taskbarMessage = "Select Order"
    if orderProg["order"] == 1:
        return render(request, 'Pizza_selection.html', {"orderNames":orderNames, "taskbarMessage":taskbarMessage, "currentOrder":currentOrder})
    else:
        outOfOrder();
        return redirect('/login')

def Crust_selection(request):
    if request.method == 'POST':
        form = buttonForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            
            if orderProg["crust"] != 1:
                outOfOrder();
                return redirect('/login')
        
            if val=="Checkout":
                orderProg["crust"] = -1;
                orderProg["Checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            elif val=="Next":
                orderProg["crust"] = -1;
                orderProg["cheese"] = 1;
                return redirect('Cheese_selection/')
            else:
                orderProg["crust"] = -1;
                orderProg["cheese"] = 1;
                currentOrder.append(val) 
                return redirect('Cheese_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=8) #Get dough
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    recipes = Recipe.objects.all() #Get all recipes objects
    for i in recipes:
        if "crust" in i.name: #find the recipes that are crusts
            name = i.name.replace("_", " ").capitalize()
            orderNames.append(name)

    taskbarMessage = "Select Crust"
    if orderProg["crust"] == 1:
        return render(request, 'Crust_selection.html', {"orderNames":orderNames, "taskbarMessage":taskbarMessage, "currentOrder":currentOrder}) 
    else:
        outOfOrder();
        return redirect('/login')
    
def Cheese_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                
            if orderProg["cheese"] != 1:
                outOfOrder();
                return redirect('/login')
            
            if val=="Checkout":
                orderProg["cheese"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            elif val=="Next":
                orderProg["cheese"] = -1;
                orderProg["sauce"] = 1;
                return redirect('Sauce_selection/')
            else:
                orderProg["cheese"] = -1;
                orderProg["sauce"] = 1;
                currentOrder.append(val) 
                return redirect('Sauce_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=3) #Get Cheese
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    taskbarMessage = "Select Cheese"
    if orderProg["cheese"] == 1:
        return render(request, 'Cheese_selection.html', {"orderNames":orderNames, "taskbarMessage":taskbarMessage, "currentOrder":currentOrder})
    else:
        outOfOrder();
        return redirect('/login')

def Sauce_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                
            if orderProg["sauce"] != 1:
                outOfOrder();
                return redirect('/login')
                
            if val=="Checkout":
                orderProg["sauce"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            elif val=="Next":
                orderProg["sauce"] = -1;
                orderProg["topping"] = 1;
                return redirect('Toppings_selection/')
            else:
                orderProg["sauce"] = -1;
                orderProg["topping"] = 1;
                currentOrder.append(val) 
                return redirect('Toppings_selection/')
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=13) #Get sauce
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    recipes = Recipe.objects.all() #Get all recipes objects
    for i in recipes:
        if "sauce" in i.name: #find the recipes that are sauces
            name = i.name.replace("_", " ").capitalize()
            orderNames.append(name)
        
    taskbarMessage = "Select Sauce"
    if orderProg["sauce"] == 1:
        return render(request, 'Sauce_selection.html', {"orderNames":orderNames,"taskbarMessage":taskbarMessage, "currentOrder":currentOrder})
    else:
        outOfOrder();
        return redirect('/login')

def Toppings_selection(request):    
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
            
            if orderProg["topping"] != 1:
                outOfOrder();
                return redirect('/login')
            
            if val=="Checkout":
                orderProg["topping"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            elif val=="Next":
                orderProg["topping"] = -1;
                orderProg["drizzle"] = 1;
                return redirect('Drizzle_selection/')
            else:
                if orderDict['numberToppings'] == 1:
                    orderProg["topping"] = -1;
                    orderProg["drizzle"] = 1;
                    currentOrder.append(val) 
                    orderDict['numberToppings'] -= 1
                    return redirect('Drizzle_selection/')
                currentOrder.append(val) 
                orderDict['numberToppings'] -= 1
                
    else:
        form = buttonForm()
        
    orderNames = []
    orders = Product.objects.filter(category_id=6) #Get meat topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    orders = Product.objects.filter(category_id=9) #Get veg topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)

    if orderProg["topping"] != 1:
        outOfOrder();
        return redirect('/login')

    if orderDict['numberToppings'] == 0:
        if currentOrder[0] == "Pepperoni pizza":
            currentOrder.append("Pepperoni") 
        orderProg["topping"] = -1;
        orderProg["drizzle"] = 1;
        return redirect('Drizzle_selection/')
    else:
        taskbarMessage = "Select Toppings"
        return render(request, 'Toppings_selection.html', {"orderNames":orderNames, "taskbarMessage":taskbarMessage, "currentOrder":currentOrder})

def Drizzle_selection(request):  
    if request.method == 'POST':
            form = buttonForm(request.POST)
            if form.is_valid():
                val = form.cleaned_data.get("btn")
                
            if orderProg["drizzle"] != 1:
                outOfOrder();
                return redirect('/login')
                
            if val=="Checkout":
                orderProg["drizzle"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.clear()
                return redirect('/customer/Crust_selection/Cheese_selection/Sauce_selection/Toppings_selection/Drizzle_selection/Checkout/')
            elif val=="Next":
                orderProg["drizzle"] = -1;
                orderProg["checkout"] = 1;
                return redirect('Checkout/')
            else:
                orderProg["drizzle"] = -1;
                orderProg["checkout"] = 1;
                currentOrder.append(val) 
                return redirect('Checkout/')
    else:
        form = buttonForm()  
        
    orderNames = []
    orders = Product.objects.filter(category_id=5) #Drizzle topping
    for i in orders:
        name = i.name.replace("_", " ").capitalize()
        orderNames.append(name)
        
    taskbarMessage = "Select Drizzle"
    if orderProg["drizzle"] == 1:
        return render(request, 'Drizzle_selection.html', {"orderNames":orderNames,"taskbarMessage":taskbarMessage, "currentOrder":currentOrder})    
    else:
        outOfOrder();
        return redirect('/login')

# Needs to display recipe if there is one 
# Need an order confirm button
# Make transaction to database
def Checkout(request):  
    
    if request.method == 'POST':
        form = buttonForm(request.POST)
            
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            
            if orderProg["checkout"] != 1:
                outOfOrder();
                return redirect('/login')
            
            if val == "Complete Order":
                orderDict["popup"] = "";
                orderDict["otherCheckoutButton"] = "none"
            
            elif val == "Order More":
                orderProg["checkout"] = -1;
                orderProg["order"] = 1;
                return redirect('/customer/')
            
            elif val == "Exit":
                fullOrder.clear()
                outOfOrder();
                return redirect('/login')
            
            elif "Cancel" in val:
                print(val)
                orderDict["popup"] = "none";
                orderDict["otherCheckoutButton"] = ""
                
            elif "Confirm Order" in val:
                customerMakeTransaction()
                fullOrder.clear()
                outOfOrder();
                return redirect('/login')                 
    
            elif "Increment Item " in val:
                itemNum = int(val.replace("Increment Item ", "").replace(" Quantity", ""))
                print(itemNum-1)
                fullOrder[itemNum -1][0] = fullOrder[itemNum -1][0] + 1
            elif "Decrement Item " in val:
                itemNum = int(val.replace("Decrement Item ", "").replace(" Quantity", ""))
                print(itemNum-1)
                if fullOrder[itemNum -1][0] > 1:
                    fullOrder[itemNum -1][0] = fullOrder[itemNum -1][0] - 1
            elif "Delete Item " in val:
                itemNum = int(val.replace("Delete Item ", ""))
                print(itemNum-1)
                fullOrder.pop(itemNum-1)
            elif "Edit Item " in val:
                orderProg["checkout"] = -1;
                orderProg["order"] = 1;
                itemNum = int(val.replace("Edit Item ", ""))
                print(itemNum-1)
                orderDict["editOrderNum"] = itemNum-1
                return redirect('/customer/')
            
            else:
                print("No match: " + val)
                
    else:
        form = buttonForm()  
   
    orderPrice = -1
    print(orderDict["editOrderNum"])     
    if (len(currentOrder) != 0):
        if orderDict["editOrderNum"] != -1:
            fullOrder[orderDict["editOrderNum"]][1] = currentOrder.copy();
            orderDict["editOrderNum"] = -1    
        else:
            orders = Product.objects.filter(category_id=2) #Get orders
            for order in orders:
                if order.name == currentOrder[0].replace(" ", "_").lower():
                    orderPrice = round(order.price, 2)
            fullOrder.append([1, currentOrder.copy(), orderPrice])  
    currentOrder.clear()
    
    total_price =0
    for order in fullOrder:
        total_price += order[0]*order[2]
        
    total_price_with_Tax = total_price + (total_price * .0825)
        
    if orderProg["checkout"] == 1:
        return render(request, 'Checkout.html', {"fullOrder": fullOrder, "total_price":round(total_price, 2),"total_price_with_Tax": round(total_price_with_Tax, 2), "currentOrder":currentOrder, "popup":orderDict["popup"], "otherCheckoutButton":orderDict["otherCheckoutButton"]})     
    else:
        outOfOrder();
        return redirect('/login')   