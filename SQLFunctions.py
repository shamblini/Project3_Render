# pip3 install psycopg

import traceback
import psycopg2
import secrets
import json
import datetime

from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe

def createTransaction(items: 'list[list[str]]'):
    '''
    Given a 2D list of items, createTransaction will calculate the total price of 
    the order and update the models to change the inventroy and transaction tables.

            Parameters:
                    `list[list[str]] items`: The items in the order

            Returns:
                    Nothing
    '''
    
    # Do nothing if there is no items
    if len(items) == 0:
        return

    # make items contain lists of equal length for SQL
    max_len = len(max(items, key=len))
    for i in items:
        while len(i) < max_len:
            i.append("-")

    itemString = "{ "
    for j in range(len(items)):
        listItem = items[j]
        listValues = "{"
        for i in range(len(listItem)):
            value = listItem[i]
            listValues += "\"" + value
            if i == len(listItem) - 1:
                listValues += "\""
            else:
                listValues += "\", "
        if j == len(items) - 1:
            listValues += "} "
        else:
            listValues += "}, "
        itemString += listValues; 
    itemString += "}"

    total = round(checkPriceCustomer(items) * 1.0825, 2)
    time = datetime.datetime.now()

    Transaction.objects.create(type=0, products=itemString, time=time, cost=total)

    recipeIngredients = {}

    # populate recipeIngredients with each unique item and its quantity
    for itemList in items:
        for item in itemList:
            if item != "-":
                if item not in recipeIngredients:
                    recipeIngredients[item] = 0
                recipeIngredients[item] += 1

    foundRecipes = {}
    ingredientsToDelete = []

    for ingredient in recipeIngredients:
        recipe = checkRecipe(ingredient)
        if recipe != None:
            for i in range(len(recipe.ingredient_list)):
                foundRecipes[recipe.ingredient_list[i]] = recipe.quantity[i] * recipeIngredients[ingredient]
            ingredientsToDelete.append(ingredient)

    for ingredient in ingredientsToDelete:
        recipeIngredients.pop(ingredient)
    
    recipeIngredients.update(foundRecipes)

    # go through ingredients and quantity, crementing the inventory 
    order_id = Category.objects.get(name="order").id

    for ingredientName in recipeIngredients:
        productToUpdate = Product.objects.get(name=ingredientName)
        if not productToUpdate.category_id == order_id:
            print(ingredientName + " Pass")
            productToUpdate.qty_stock = productToUpdate.qty_stock - recipeIngredients[ingredientName]
            productToUpdate.save()

def createRestock(name: str, quantity: int):
    '''
    Given a restock order, createTransaction will update the models to change 
    the inventroy and transaction tables and calculate the total price of the restock.

            Parameters:
                    `str name`: The ingredient being restocked
                    `int quantity`: Quantity of restock
                    `str total`: The total cost of the restock order

            Returns:
                    Nothing
    '''
    time = datetime.datetime.now()

    product = '{ {\"' + name + '\"} }'

    total = checkPriceManager(name, quantity)
    print(total)
    Transaction.objects.create(type=1, products=product, time=time, cost=total)

    productToUpdate = Product.objects.get(name=name)
    productToUpdate.qty_stock = productToUpdate.qty_stock + quantity
    productToUpdate.save()

def checkRecipe(name: str) -> dict:
    '''
    checkRecipes checks the recipe objects from the recipe models for a given recipe and returns its ingredients

            Parameters:
                    `str name`: The name of the recipe

            Returns:
                    The recipe data as a `dictionary` if name is in recipes.objects, otherwise `None`
    '''

    try:
        recipe = Recipe.objects.get(name=name)
    except:
        # traceback.print_exc()
        return None

    return recipe

def checkPriceCustomer(ingredients: 'list[list[str]]') -> float:
    '''
    checkPriceCustomer will check the products models given a matrix of ingredients and return the cost of the order

            Parameters:
                    `list[list[str]] ingredients`: 2D List of ingredients in the order

            Returns:
                    The cost of the order as a `float` including tax
    '''
    total = 0.0

    order_id = Category.objects.get(name="order").id

    for ingredient_list in ingredients:
        for ingredient_name in ingredient_list:
            ingredient = ""
            try:
                ingredient = Product.objects.get(name=ingredient_name)
            except:
                # traceback.print_exc()
                continue
            if ingredient.category_id == order_id or ingredient.category_id == 8:
                total += ingredient.price

    return total

def checkPriceManager(name: str, quantity: int) -> float:
    '''
    checkPriceManager will check all product objects and return the cost of the restock order

            Parameters:
                    `str name`: Name of the item being restocked
                    `int quantity`: Quantity of the restock

            Returns:
                    The cost of the restock as a `float`
    '''
    total = 0.0

    ingredient = ""
    try:
        print(name)
        ingredient = Product.objects.get(name=name)
    except:
        # traceback.print_exc()
        return total

    total += ingredient.price * quantity
    return total
    

# deprecated functions:
def crementIngredient(name: str, quantity: int, increment: bool):
    '''
    THIS FUNCTION IS DEPRECATED
    Given an inventory change, crementIngredient will create the SQL commands to update 
    the inventroy and write them to databaseCommands.txt

            Parameters:
                    `str name`: The ingredient being cremented
                    `int quantity`: Quantity of crement
                    `bool increment`: True if the ingredient quantity is being added to

            Returns:
                    Nothing
    '''
        
    # Solve for new ingredientName quantity (math)
    sqlStatement = ""
    if increment:
        sqlStatement = "UPDATE inventory SET quantity= quantity + (" + str(quantity) + " * unit) WHERE ingredient=\'" + name + "\';"
    else:
        sqlStatement = "UPDATE inventory SET quantity= quantity - (" + str(quantity) + " * unit) WHERE ingredient=\'" + name + "\';"
    
    # Update ingredientName quantity in inventory (stmt)
    commandFile = open("databaseCommands.txt", "a")
    commandFile.write(sqlStatement + "\n")
    commandFile.close()

def updateDatabase():
    '''
    THIS FUNCTION IS DEPRECATED
    updateDatabase will execute all of the SQL commands in `databaseCommands.txt` and output them to `commands.log`

            Parameters:
                    None

            Returns:
                    Nothing
    '''

    databaseCommands = open("databaseCommands.txt", "r+")
    sqlStatement = databaseCommands.read()
    performQuery(sqlStatement)

    commandLog = open("commands.log", "a")
    commandLog.write(sqlStatement)
    commandLog.write("Database Updated\n")
    commandLog.close()

    databaseCommands.truncate(0)
    databaseCommands.close()

def saveRecipes():
    '''
    THIS FUNCTION IS DEPRECATED
    saveRecipes will output all recipe data into `recipes.json`

            Parameters:
                    None

            Returns:
                    Nothing
    '''
    recipes = {}

    sqlStatement = "SELECT * FROM recipe;"
    result = performQuery(sqlStatement)

    for recipe in result:
        temp_recipe = {}
        temp_recipe["id"] = recipe[0]
        temp_recipe["ingredients"] = recipe[2]
        temp_recipe["quantity"] = recipe[3]
        recipes[recipe[1]] = temp_recipe

    f = open("recipes.json", "w")
    f.write(json.dumps(recipes, indent=4))
    f.close

def saveIngredients():
    '''
    THIS FUNCTION IS DEPRECATED
    saveIngredients will output all inventory data into `ingredients.json`

            Parameters:
                    None

            Returns:
                    Nothing
    '''
    ingredients = {}

    sqlStatement = "SELECT * FROM Inventory;"
    result = performQuery(sqlStatement)

    for ingredient in result:
        temp_ingredient = {}
        temp_ingredient["id"] = ingredient[0]
        temp_ingredient["quantity"] = ingredient[2]
        temp_ingredient["unit"] = ingredient[3]
        temp_ingredient["cost"] = ingredient[4]
        temp_ingredient["item_type"] = ingredient[5]
        ingredients[ingredient[1]] = temp_ingredient

    f = open("ingredients.json", "w")
    f.write(json.dumps(ingredients, indent=4))
    f.close

def performQuery(QueryString, printStatus=False):
    '''
    THIS FUNCTION IS DEPRECATED
    Given a SQL query, performQuery will execute the SQL query and return its results.

            Parameters:
                    `str QueryString`: The SQL query.
                    `bool printStatus`: Will print a status message to the terminal if `True`.

            Returns:
                    `List` if query has results, `"FAIL"` if the query failed, otherwise `None`.
    '''
    try:
        # make initial connection
        conn = psycopg2.connect(
            host=secrets.GetSecret('hostname'),
            dbname=secrets.GetSecret('database'),
            user=secrets.GetSecret('username'),
            password=secrets.GetSecret('pwd')
        )

        # cursors are used to perform queries 
        cur = conn.cursor()
        
        cur.execute(QueryString) # Performs the query
        # return cur.fetchall()
        conn.commit()
        
        if printStatus == True:
            print("performQuery: " , cur.statusmessage)
            
        if (cur.description == None):
            return None
        else:
            return cur.fetchall()
    
    except:
        print("DB conn failed\n")
        traceback.print_exc()
        return "FAIL"
        
    finally:
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()