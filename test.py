import SQLFunctions
import analytics

# updates database for a restock of an item given the name and quantity
SQLFunctions.createRestock("coffee", 2)

# # list of items in an order
items = [["cheese_pizza", "coffee", "zesty_Red", "bottled_drink"], ["pepperoni_pizza", "soda", "bottled_drink"]]

# updates database for an order given the items
SQLFunctions.createTransaction(items)

# salesList = analytics.salesReport("2022-10-01", "2022-10-20")

# excessList = analytics.salesReport("2022-10-01")

# restockList = analytics.restockReport("2022-10-01", "2022-10-20")

# pairList = analytics.sellPairs("2022-10-01", "2022-10-20")

