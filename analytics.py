from DBModels.models import Category, Employee, Job, Product, Transaction, Type, Customer, Recipe
from datetime import datetime

def salesReport(startTime: str, endTime: str) -> dict:
    '''
    Retrieves a sales report from the database in a given time window

            Parameters:
                    str startTime start time of the sales report
                    str endTime end time of the sales report

            Returns: 
                    map of items and quantity sold from startTime to endTime
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

def excessReport(startTime: str) -> 'list[str]':
    '''
     Finds items in the inventory that sold less than 10% of their quantity in a given time window

            Parameters:
                    str startTime start time of the excess report

            Returns: 
                    map of items and remaining quantity from startTime to endTime
     */
     '''
    date = datetime.today().strftime('%Y-%m-%d')
    orderData = salesReport(startTime, date)
    ans = []

    excessMap = {}

    inventory = Product.objects.exclude(name="Order")

    for i in inventory:
        excessMap[i.name] = i.qty_stock * .10

    for item in orderData:
        if item in excessMap and orderData[item] < excessMap[item]:
            ans.append(item)
    
    return ans

def restockReport() -> 'list[str]':
    '''
    Finds items in the inventory that have sold more than the remaining quantity in a given time window

            Returns: 
                    list of low items and quantity remaining

    '''
    earliest = Transaction.objects.order_by('time')[0].time
    date = datetime.today().strftime('%Y-%m-%d')
    orderData = salesReport(earliest, date)
    ans = []

    for item in orderData:
        if orderData[item] < 30:
            ans.append(item)
    
    return ans

def sellPairs(startTime: str, endTime: str) -> 'list[str]':
    '''
    Finds items in the inventory that sell together the most commonly in a given time window

            Parameters:
                    str startTime start time of the pairs report
                    str endTime end time of the pairs report

            Returns: 
                    a list of pairs of ingredients
    '''

    largestPairs = []
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
                        pair = itemList[j] + " " + itemList[i]
                        if itemList[i] > itemList[j]:
                            pair = itemList[i] + " " + itemList[j]

                        if pair not in pairMap:
                            pairMap[pair] = 0
                        pairMap[pair] += 1


    while len(pairMap) > 0:
        largest = -1
        largestName = ""
        for i in pairMap:
            if largest < pairMap[i]:
                largest = pairMap[i]
                largestName = i
        
        largestPairs.append(largestName + " " + str(largest))
        pairMap.pop(largestName)
    
    return largestPairs