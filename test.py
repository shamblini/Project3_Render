import SQLFunctions

# updates database for a restock of an item given the name and quantity
SQLFunctions.createRestock("coffee", 2)

# # list of items in an order
items = [["cheese_pizza", "coffee", "zesty_Red", "bottled_drink"], ["pepperoni_pizza", "soda", "bottled_drink"]]

# updates database for an order given the items
SQLFunctions.createTransaction(items)
