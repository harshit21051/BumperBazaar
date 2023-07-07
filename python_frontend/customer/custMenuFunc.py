import index, os
import customer.custLogin as custLogin

def browseProd(csr, custID):
    os.system('cls')
    csr.execute(f'''
        SELECT ProdName, ProdID, Price FROM Inventory
    ''')
    items = csr.fetchall()
    print(" Available items :")
    for x in items:
        print()
        print(f"  {x[0]}")
        print(" ------------------------------------")
        print(f"  Product ID  :\t{x[1]}")
        print(f"  Price       :\t{x[2]}")
    index.printformat()
    custLogin.custMenu(csr, custID)

def viewCart(csr, custID):
    os.system('cls')
    csr.execute(f'''
        SELECT ProdName, ProdID, Price, Qty
        FROM Inventory NATURAL JOIN Cart
        WHERE CustID = {custID}
    ''')
    items = csr.fetchall()
    if (len(items) == 0):
        print(" Cart empty !!")
    else:
        print(" Items in your cart :")
        for x in items:
            print()
            print(f"  {x[0]}")
            print(" ------------------------------------")
            print(f"  Product ID  :\t{x[1]}")
            print(f"  Price       :\t{x[2]}")
            print(f"  Qty         :\t{x[3]}")
    index.printformat()
    custLogin.custMenu(csr, custID)

def profile(csr, custID):
    os.system('cls')
    csr.execute(f'''
        SELECT * FROM Customers
        WHERE CustID = {custID}
    ''')
    x = csr.fetchall()
    print("  Profile\n  ----------\n")
    print(f"  Name              : {x[0][1]}")
    print()
    print(f"  Gender            : {x[0][2]}")
    print()
    print(f"  Category          : {x[0][3]}")
    print()
    print(f"  Email             : {x[0][4]}")
    print()
    print(f"  Phone             : {x[0][5]}")
    print()
    print(f"  Wallet Balance    : {x[0][6]}")
    index.printformat()
    custLogin.custMenu(csr, custID)

def addAmt(csr, custID):
    amt = int(input(" Enter amount to add : "))
    csr.execute(f'''
        UPDATE Customers
        SET WalletBalance = WalletBalance + {amt}
        WHERE CustID = '{custID}'
    ''')
    print("\n Amount successfully added !!")
    index.printformat()
    custLogin.custMenu(csr, custID)

def addCart(csr, custID):
    prodID = int(input(" Enter Product ID : "))
    print()
    qty = int(input(" Enter quantity   : "))
    csr.execute(f'''
        SELECT * FROM Inventory
        WHERE ProdID = {prodID}
    ''')
    item = csr.fetchall()
    if (len(item) == 0):
        print("\n Sorry! Product not available")
    else:
        csr.execute(f"INSERT INTO Cart VALUES ({custID}, {prodID}, {qty})")
        print("\n Product successfully added to cart.")
    index.printformat()
    custLogin.custMenu(csr, custID)

def emptyCart(csr, custID):
    csr.execute(f'''
        SELECT * FROM Cart
        WHERE CustID = {custID}
    ''')
    items = csr.fetchall()
    if (len(items) == 0):
        print(" Cart empty !!")
    else:
        csr.execute(f"DELETE FROM Cart WHERE CustID = {custID}")
        print(" Cart successfully emptied.")
    index.printformat()
    custLogin.custMenu(csr, custID)

def checkoutCart(csr, custID):
    csr.execute(f'''
        SELECT WalletBalance FROM Customers
        WHERE CustID = {custID}
    ''')
    wallet = csr.fetchall()
    for i in wallet:
        for x in i:
            wallet = x
    csr.execute(f'''
        SELECT sum(Price * Qty)
        FROM Inventory NATURAL JOIN Cart
        GROUP BY CustID
        HAVING CustID = {custID}
    ''')
    totAmt = csr.fetchall()
    if len(totAmt) == 0:
        print(f" Cart empty!")
    else:
        for i in totAmt:
            for x in i:
                totAmt = x
        print(f" Total amount : {totAmt}\n")
        categ = getCateg(csr, custID)
        discPerc = 10
        if categ.lower() == 'prime':
            discPerc = 30
        elif categ.lower() == 'elite':
            discPerc = 50
        discAmt = (100 - discPerc) * (totAmt/100)
        print(f" Discount for {categ.upper()} : {discPerc}%\n")
        print(f" Amount after discount : {discAmt}\n")
        opt = input(f" Proceed to checkout (Y/N) : ")
        if opt.lower() == 'y':
            print("\n Payment mode")
            print()
            print(" 1) Cash")
            print(" 2) Wallet")
            print()
            opt = int(input(" Enter option : "))
            index.printformat()
            if (opt == 1):
                csr.execute(f'''
                    UPDATE Inventory, Cart
                    SET StockQty = StockQty - Cart.qty
                    WHERE Inventory.ProdID = Cart.ProdID AND Cart.CustID = {custID}
                ''')
                csr.execute(f'''
                    INSERT INTO Orders
                        (CustID, PayMode, Amount, Status)
                    VALUES
                        ({custID}, 'Cash', {discAmt}, 'Placed')
                ''')
                print(" Order placed successfully !!")
            elif (opt == 2):
                if (wallet >= totAmt):
                    csr.execute(f'''
                        UPDATE Inventory, Cart
                        SET StockQty = StockQty - Cart.qty
                        WHERE Inventory.ProdID = Cart.ProdID AND Cart.CustID = {custID}
                    ''')
                    csr.execute(f'''
                        UPDATE Customers
                        SET WalletBalance = WalletBalance - {totAmt}
                        WHERE CustID = '{custID}'
                    ''')
                    csr.execute(f'''
                        INSERT INTO Orders
                            (CustID, PayMode, Amount, Status)
                        VALUES
                            ({custID}, 'Wallet', {discAmt}, 'Placed')
                    ''')
                    print(" Order placed successfully !!")
                else:
                    print(" Insufficient wallet balance !!")
    index.printformat()
    custLogin.custMenu(csr, custID)

def viewOrders(csr, custID):
    os.system('cls')
    csr.execute(f'''
        SELECT OrderID, Status
        FROM Orders
        WHERE CustID = {custID}
    ''')
    orders = csr.fetchall()
    if (len(orders) == 0):
        print(" No orders !!")
    else:
        print(" Your orders :")
        for x in orders:
            print()
            print(f"  Order ID  :\t{x[0]}")
            print(f"  Status    :\t{x[1]}")
    index.printformat()
    custLogin.custMenu(csr, custID)

def getCateg(csr, custID):
    csr.execute(f'SELECT Category FROM Customers WHERE CustID = {custID}')
    categ = csr.fetchall()
    for i in categ:
        for x in i:
            categ = x
    return categ

def changeCateg(csr, custID):
    print(f" Choose from below:")
    print()
    print("   1)  Normal")
    print("   2)  Prime")
    print("   3)  Elite")
    opt = int(input("\n Enter option : "))
    newCateg = 'Normal'
    cost = 100
    if (opt == 2):
        newCateg = 'Prime'
        cost = 500
    elif (opt == 3):
        newCateg = 'Elite'
        cost = 1000
    oldCateg = getCateg(csr, custID)
    if oldCateg.lower() == newCateg.lower():
        print("\n Sorry! Same category")
    else:
        csr.execute(f'''
            UPDATE Customers
            SET Category = '{newCateg}', WalletBalance = WalletBalance - {cost}
            WHERE CustID = '{custID}'
        ''')
        print(f"\n Changed successfully!\n\n Deducted an amount of Rs. {cost}.")
    index.printformat()
    custLogin.custMenu(csr, custID)
