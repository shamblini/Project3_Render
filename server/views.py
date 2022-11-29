# Create your views here.
from django.shortcuts import render
from .forms import buttonForm
from .models import Product, Recipe
from collections import defaultdict
import SQLFunctions

products = Product.objects.all()
recipes = Recipe.objects.all()

bottled_drink = []
meat_topping = []
sauce_base = []
dough_base = []
dough = []
drizzle_topping = []
cheese = []
order = []
special = []
fountain_drink = []
veg_topping = []

currentOrder = []
totalOrder = []

base_control = True
bd_control = True
fd_control = True
cp_control = True
pp_control = True
ot_control = True
ft_control = True

toppingCount = 0
topMax = 0

def initializeLists():
    for product in products:
        match product.category_id:
            case 3:
                order.append(product)
            case 6:
                meat_topping.append(product)
            case 8:
                sauce_base.append(product)
            case 9:
                veg_topping.append(product)
initializeLists()

# Create your views here.
def serverScreen(request):
    if(request.session['base_control'] == None):
        request.session['base_control'] = True
        request.session['bd_control'] = True
        request.session['fd_control'] = True
        request.session['cp_control'] = True
        request.session['pp_control'] = True
        request.session['ot_control'] = True
        request.session['ft_control'] = True
        request.session['toppingCount'] = 0
        request.session['topMax'] = 0
        request.session['totalOrder'] = totalOrder.copy()

    if request.method == 'POST':
        form = buttonForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data.get("btn")
            match item:
                case 'cheese_pizza':
                    request.session['base_control'] = False
                    currentOrder.append(item) 
                case 'pepperoni_pizza':
                    request.session['base_control'] = False   
                    currentOrder.append(item)  
                case 'one_topping':
                    request.session['base_control'] = False
                    request.session['ot_control'] = False
                    request.session['topMax'] = 1
                    currentOrder.append(item) 
                case 'four_topping':
                    request.session['base_control'] = False
                    request.session['ft_control'] = False
                    request.session['topMax'] = 4
                    currentOrder.append(item) 
                case 'fountain_drink':
                    request.session['fd_control'] = False
                case 'bottled_drink':
                    request.session['bd_control'] = False
                    currentOrder.append(item) 
                case "regular_crust":
                    for val in recipes.filter(name="regular_crust").values():
                        for ing in val['ingredient_list']:
                            currentOrder.append(ing)
                case "alfredo":
                    for val in recipes.filter(name="alfredo").values():
                        for ing in val['ingredient_list']:
                            currentOrder.append(ing)
                case "zesty_Red":
                    for val in recipes.filter(name="zesty_Red").values():
                        for ing in val['ingredient_list']:
                            currentOrder.append(ing)
                case "New Pizza":
                    if(len(currentOrder.copy()) != 0):
                        totalOrder.append(currentOrder.copy())
                    request.session['totalOrder'] = totalOrder.copy()
                    print(totalOrder)

                    currentOrder.clear()
                    request.session['base_control'] = True
                    request.session['bd_control'] = True
                    request.session['fd_control'] = True
                    request.session['cp_control'] = True
                    request.session['pp_control'] = True
                    request.session['ot_control'] = True
                    request.session['ft_control'] = True
                    request.session['toppingCount'] = 0
                    request.session['topMax'] = 0
                case "Confirm Order":
                    if(len(currentOrder.copy()) != 0):
                        totalOrder.append(currentOrder.copy())
                    request.session['totalOrder'] = totalOrder.copy()
                    print("Total Order: ")
                    print(totalOrder)

                    SQLFunctions.createTransaction(totalOrder)

                    request.session['base_control'] = True
                    request.session['bd_control'] = True
                    request.session['fd_control'] = True
                    request.session['cp_control'] = True
                    request.session['pp_control'] = True
                    request.session['ot_control'] = True
                    request.session['ft_control'] = True
                    request.session['toppingCount'] = 0
                    request.session['topMax'] = 0

                    currentOrder.clear()
                    totalOrder.clear()
                case "Clear Order":
                    request.session['base_control'] = True
                    request.session['bd_control'] = True
                    request.session['fd_control'] = True
                    request.session['cp_control'] = True
                    request.session['pp_control'] = True
                    request.session['ot_control'] = True
                    request.session['ft_control'] = True
                    request.session['toppingCount'] = 0
                    request.session['topMax'] = 0
                    
                    totalOrder.clear()
                    currentOrder.clear()
                    request.session['totalOrder'].clear()  
                case _:   
                    currentOrder.append(item)
                    for m in meat_topping:
                        if(m.name == item):
                            print(item)
                            request.session['toppingCount'] += 1
                    for v in veg_topping:
                        if(v.name == item):
                            request.session['toppingCount'] += 1
 
            print(currentOrder)
            
    else:
        form = buttonForm()


    return render(request, 'html/serverScreen.html', {
        'products':products, 'bd_control':request.session['bd_control'], 'fd_control':request.session['fd_control'],
        'cp_control':request.session['cp_control'], 'pp_control':request.session['pp_control'], 
        'ot_control':request.session['ot_control'], 'ft_control':request.session['ft_control'], 
        'base_control':request.session['base_control'], 'totalOrder':request.session['totalOrder'],
        'toppingCount':request.session['toppingCount'],'topMax':request.session['topMax'],
        })

