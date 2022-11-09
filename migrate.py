import SQLFunctions

id = SQLFunctions.performQuery("SELECT id FROM Inventory")
name = SQLFunctions.performQuery("SELECT ingredient FROM Inventory")
quantity = SQLFunctions.performQuery("SELECT quantity FROM Inventory")
unit = SQLFunctions.performQuery("SELECT unit FROM Inventory")
cost = SQLFunctions.performQuery("SELECT cost FROM Inventory")
type = SQLFunctions.performQuery("SELECT item_type FROM Inventory")

employees = SQLFunctions.performQuery("SELECT * FROM Employee")

# migrate item_types
t_set = set({})
counter = 1
for t in type:
    if t not in t_set:
        sqlStatement = "INSERT INTO p3_category (category_id, name)";     
        sqlStatement += " VALUES (" + str(counter) + ", " + str(t)[1:-2] + ")"
        SQLFunctions.performQuery(sqlStatement)
        print(sqlStatement)
        t_set.add(t)
        counter += 1

# migrate inventory
for i in range(len(id)):
    temp_id = SQLFunctions.performQuery("SELECT category_id FROM p3_category WHERE name = '" + type[i][0] + "'")[0]
    sqlStatement = "INSERT INTO p3_product (product_id, name, qty_stock, price, category_id)";    
    quant = float(str(quantity[i])[1:-2])
    u = float(str(unit[i])[1:-2])
    c = float(str(cost[i])[1:-2])
    if u == 0: u = 1

    sqlStatement += " VALUES ({p_id}, '{name}', {stock:.2f}, {price:.2f}, {c_id})".format(p_id=id[i][0], name=name[i][0], stock=(quant * u), price=(c), c_id=temp_id[0])
    SQLFunctions.performQuery(sqlStatement)
    print(sqlStatement)

# migrate employees
for employee in employees:
    first_name = employee[2].split(" ")[0]
    last_name = employee[2].split(" ")[1]
    email = first_name + last_name + "@gmail.com"
    sqlStatement = "INSERT INTO p3_employee (employee_id, first_name, last_name, email, phone_number, job_id, hired_date, location_id)";    
    sqlStatement += " VALUES ({id}, '{fname}', '{lname}', '{email}', {pnum}, {job_id}, '{hired_date}', {lid})".format(
    id=employee[0], fname=first_name, lname=last_name, email=email, pnum=0, job_id=0, hired_date=employee[7], lid=0)
    SQLFunctions.performQuery(sqlStatement)
    print(sqlStatement)