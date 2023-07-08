import index, os, time
import admin.adminLogin as adminLogin

def endFunction(csr, adminID):
    csr.execute("COMMIT")
    index.printformat()
    print(" 1) Back")
    print(" 2) Logout")
    print(" 3) Exit")
    opt = int(input(" Enter option : "))
    if (opt == 2):
        return index.start(csr)
    elif (opt == 3):
        print("\n Thank you and visit again.")
        index.printformat()
        time.sleep(0.6)
        exit()
    else:
        index.printformat()
        adminLogin.adminMenu(csr, adminID)

def viewInv(csr, adminID):
    os.system('cls')
    print()
    csr.execute(f'''
        SELECT ProdName, ProdID, Price, StockQty FROM Inventory
    ''')
    items = csr.fetchall()
    print(" Available items :")
    for x in items:
        print()
        print(f"  {x[0]}")
        print(" ------------------------------------")
        print(f"  Product ID  :\t{x[1]}")
        print(f"  Price       :\t{x[2]}")
        print(f"  Stock Qty   :\t{x[3]}")
    endFunction(csr, adminID)

def addInv(csr, adminID):
    name = input(" Enter Product name   : ")
    print()
    price = int(input( " Enter price          : "))
    print()
    qty = int(input(   " Enter stock quantity : "))
    csr.execute(f'''
        INSERT INTO Inventory (ProdName, Price, StockQty)
        VALUES ('{name}', {price}, {qty})
    ''')
    print("\n -------------------------------------------")
    print("\n Product successfully added to inventory.")
    endFunction(csr, adminID)

def remInv(csr, adminID):
    prodID = int(input( " Enter product ID : "))
    csr.execute(f'''
        SELECT * FROM Inventory
        WHERE ProdID = {prodID}
    ''')
    items = csr.fetchall()
    print("\n --------------------------------------------")
    if (len(items) == 0):
        print("\n Product doesn't exist in inventory !!")
    else:
        csr.execute(f"DELETE FROM Inventory WHERE ProdID = {prodID}")
        print("\n Product successfully removed from inventory.")
    endFunction(csr, adminID)

def updStock(csr, adminID):
    prodID = int(input(" Enter product ID      : "))
    print()
    qty = int(input(" Enter stock quantity  : "))
    csr.execute(f'''
        SELECT * FROM Inventory
        WHERE ProdID = {prodID}
    ''')
    items = csr.fetchall()
    print("\n --------------------------------------------")
    if (len(items) == 0):
        print("\n Product doesn't exist in inventory !!")
    else:
        csr.execute(f'''
            UPDATE Inventory
            SET StockQty = {qty}
            WHERE ProdID = {prodID}
        ''')
        print("\n Product stock successfully updated.")
    endFunction(csr, adminID)

def updPrice(csr, adminID):
    prodID = int(input(" Enter product ID  : "))
    print()
    price = int(input(" Enter price       : "))
    csr.execute(f'''
        SELECT * FROM Inventory
        WHERE ProdID = {prodID}
    ''')
    items = csr.fetchall()
    print("\n --------------------------------------------")
    if (len(items) == 0):
        print("\n Product doesn't exist in inventory !!")
    else:
        csr.execute(f'''
            UPDATE Inventory
            SET Price = {price}
            WHERE ProdID = {prodID}
        ''')
        print("\n Product price successfully updated.")
    endFunction(csr, adminID)

def viewCust(csr, adminID):
    os.system('cls')
    print()
    print("  View customer details:")
    csr.execute("SELECT count(*) FROM CUSTOMERS")
    count = csr.fetchall()
    for i in count:
        for x in i:
            count = x
    first = 1000
    last = first + count - 1
    print(f"\n  -> Total number of customers : {count}")
    print(f"\n  -> First Customer ID : {first}")
    print(f"\n  -> Last Customer ID : {last}\n")
    custID = int(input("\n  Enter customer ID : "))
    csr.execute(f'''
        SELECT * FROM Customers
        NATURAL JOIN Address
        NATURAL JOIN Accounts
        WHERE CustID = {custID}
    ''')
    items = csr.fetchall()
    if (len(items) == 0):
        print("\n  Invalid ID!")
    else:
        print("\n\n  Customer details :")
        for x in items:
            print()
            print(f"  {x[1]}")
            print(" -------------------------------------------------")
            print(f"  Gender          :\t{x[2]}")
            print(f"  Category        :\t{x[3]}")
            print(f"  Email           :\t{x[4]}")
            print(f"  Phone           :\t{x[5]}")
            print(f"  Wallet balance  :\t{x[6]}")
            print("\n -- Address --------------------------------------")
            print(f"  House           :\t{x[7]}")
            print(f"  Street          :\t{x[8]}")
            print(f"  City            :\t{x[9]}")
            print("\n -- Account --------------------------------------")
            print(f"  Username        :\t{x[10]}")
            print(f"  Password        :\t{x[11]}")
    endFunction(csr, adminID)

def viewOrders(csr, adminID):
    os.system('cls')
    print()
    csr.execute(f'''
        SELECT * FROM Orders
    ''')
    orders = csr.fetchall()
    if (len(orders) == 0):
        print(" No orders to show !!")
    else:
        print(" Orders :")
        for x in orders:
            print()
            print(" ------------------------------------")
            print(f"  Order ID     :\t{x[0]}")
            print(f"  Customer ID  :\t{x[1]}")
            print(f"  Payment mode :\t{x[2]}")
            print(f"  Amount       :\t{x[3]}")
            print(f"  Status       :\t{x[4]}")
    endFunction(csr, adminID)

def changeOrderStatus(csr, adminID):
    orderID = int(input(" Enter order ID                           : "))
    print()
    status = input(" Enter status (Placed/Shipped/Delivered)  : ")
    csr.execute(f'''
        UPDATE Orders
        SET Status = '{status}'
        WHERE OrderID = {orderID}
    ''')
    print("\n Order status successfully updated.")
    endFunction(csr, adminID)

def viewAccStmt(csr, adminID):
    os.system('cls')
    print()
    csr.execute(f'''
        SELECT sum(Price * StockQty) FROM Inventory;
    ''')
    totGoodsVal = csr.fetchall()
    for i in totGoodsVal:
        for x in i:
            totGoodsVal = x
    csr.execute(f'''
        SELECT sum(Amount) FROM Orders
        WHERE PayMode = 'Wallet' OR Status = 'Delivered';
    ''')
    totIncome = csr.fetchall()
    for i in totIncome:
        for x in i:
            totIncome = x
    print(f" Account statement:")
    print(f"\n Total goods value : {totGoodsVal}")
    print(f"\n Total income      : {totIncome}")
    endFunction(csr, adminID)
