from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe
from datetime import datetime

def salesReport(startTime: str, endTime: str) -> dict:
    '''
     Retrieves a sales report from the database in a given time window
     @param startTime start time of the sales report
     @param endTime end time of the sales report
     @return returns a list of transactions from startTime to endTime
    '''

    orderData = Transaction.objects.filter(time__range=[startTime, endTime])

    itemMap = {}

    inventory = Product.objects.exclude(category_id=3)

    for i in inventory:
        itemMap[i.name] = 0

    for itemLists in orderData:
        for itemList in itemLists.products:
            for item in itemList:
                if item != "-":
                    if item not in itemMap:
                        continue
                    itemMap[item] += 1
    
    sortedMap = {}

    while len(itemMap) > 0:
        largest = -1
        largestName = ""
        for i in itemMap:
            if largest < itemMap[i]:
                largest = itemMap[i]
                largestName = i
        
        sortedMap[largestName] = largest
        itemMap.pop(largestName)
    
    return sortedMap

def excessReport(startTime: str) -> dict:
    '''
     Finds items in the inventory that sold less than 10% of their quantity in a given time window
     @param startTime start time of the transactions to search
     @param endTime end time of the transactions to search
     @return returns a list of ingredients
     */
     '''
    date = datetime.today().strftime('%Y-%m-%d')
    orderData = salesReport(startTime, date)
    ans = {}

    excessMap = {}

    inventory = Product.objects.exclude(name="Order")

    for i in inventory:
        excessMap[i.name] = i.qty_stock * .10

    for item in orderData:
        if item in excessMap and orderData[item] < excessMap[item]:
            ans[item] = orderData[item]
    
    return ans

def restockReport() -> dict:
    '''
    Finds items in the inventory that have sold more than the remaining quantity in a given time window
    @param startTime start time of the transactions to search
    @param endTime end time of the transactions to search
    @return returns a list of ingredients

    '''
    ans = {}

    order_id = Category.objects.get(name="order").id
    products = Product.objects.exclude(category_id=order_id)

    for item in products:
        if item.qty_stock < 30:
            ans[item] = item.qty_stock
    
    return ans

def sellPairs(startTime: str, endTime: str) -> dict:
    '''
    Finds items in the inventory that sell together the most commonly in a given time window
    @param startTime start time of the transactions to search
    @param endTime end time of the transactions to search
    @return returns a list of pairs of ingredients
    '''

    largestPairs = {}
    pairMap = {}
    inventory = Product.objects.exclude(category_id=3)
    recipes = Recipe.objects.all()

    validItems = []

    for i in inventory:
        validItems.append(i.name)

    for i in recipes:
        validItems.append(i.name)

    orderData = Transaction.objects.filter(time__range=[startTime, endTime])

    for itemLists in orderData:
        for itemList in itemLists.products:
            for i in range(len(itemList)):
                for j in range(i + 1, len(itemList)):
                    if itemList[i] in validItems and itemList[j] in validItems:
                        pair = (itemList[j], itemList[i])
                        if itemList[i] > itemList[j]:
                            pair = (itemList[i], itemList[j])

                        if pair not in pairMap:
                            pairMap[pair] = 0
                        pairMap[pair] += 1


    while len(pairMap) > 0:
        largest = -1
        largestName = ("","")
        for i in pairMap:
            if largest < pairMap[i]:
                largest = pairMap[i]
                largestName = i
        
        largestPairs[largestName] = largest
        # largestPairs.append(largestName + " " + str(largest))
        pairMap.pop(largestName)
    
    return largestPairs