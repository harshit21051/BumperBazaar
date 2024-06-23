import index, os, time
import customer.custLogin as custLogin

def getCustInfo(csr, custID):
    csr.execute(f'''
        SELECT * FROM Customers NATURAL JOIN Address NATURAL JOIN Accounts
        WHERE CustID = {custID}
    ''')
    result = csr.fetchall()
    if result:
        return {
            'Name': result[0][1],
            'Gender': result[0][2],
            'Category': result[0][3],
            'Email': result[0][4],
            'Phone': result[0][5],
            'WalletBalance': result[0][6],
            'House': result[0][7],
            'Street': result[0][8],
            'City': result[0][9],
            'Username': result[0][10],
            'Password': result[0][11]
        }
    else: return None

def endFunction(csr, custID):
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
        custLogin.custMenu(csr, custID)

def browseProd(csr, custID):
    os.system('cls')
    print()
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
    endFunction(csr, custID)

def searchProd(csr, custID):
    os.system('cls')
    print()
    query = input(" Search for product : ")
    csr.execute(f'''
        SELECT ProdName, ProdID, Price FROM Inventory
        WHERE ProdName LIKE '%{query}%'
    ''')
    items = csr.fetchall()
    if (len(items) == 0):
        print("\n No results found!")
    else:
        print("\n Search results :")
        for x in items:
            print()
            print(f"  {x[0]}")
            print(" ------------------------------------")
            print(f"  Product ID  :\t{x[1]}")
            print(f"  Price       :\t{x[2]}")
    endFunction(csr, custID)

def viewCart(csr, custID):
    os.system('cls')
    print()
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
    endFunction(csr, custID)

def profile(csr, custID):
    os.system('cls')
    print()
    print("  Profile\n  ----------\n")
    print(f"  Name              : {getCustInfo(csr,custID)['Name']}")
    print()
    print(f"  Gender            : {getCustInfo(csr,custID)['Gender']}")
    print()
    print(f"  Category          : {getCustInfo(csr,custID)['Category']}")
    print()
    print(f"  Email             : {getCustInfo(csr,custID)['Email']}")
    print()
    print(f"  Phone             : {getCustInfo(csr,custID)['Phone']}")
    print()
    print(f"  Username          : {getCustInfo(csr,custID)['Username']}")
    print()
    print(f"  Address           : {getCustInfo(csr,custID)['House']}")
    print(f"                      {getCustInfo(csr,custID)['Street']}")
    print(f"                      {getCustInfo(csr,custID)['City']}")
    print()
    print(f"  Wallet Balance    : {getCustInfo(csr,custID)['WalletBalance']}")
    endFunction(csr, custID)

def addAmt(csr, custID):
    os.system('cls')
    amt = int(input("\n Enter amount to add : "))
    csr.execute(f'''
        UPDATE Customers
        SET WalletBalance = WalletBalance + {amt}
        WHERE CustID = {custID}
    ''')
    print("\n Amount successfully added !!")
    endFunction(csr, custID)

def addCart(csr, custID):
    prodID = int(input(" Enter Product ID : "))
    print()
    qty = int(input(" Enter quantity   : "))
    csr.execute(f'''
        SELECT * FROM Inventory
        WHERE ProdID = {prodID}
    ''')
    item = csr.fetchall()
    csr.execute(f'''
        SELECT * FROM Cart
        WHERE ProdID = {prodID} AND CustID = {custID}
    ''')
    exist = csr.fetchall()
    if (len(item) == 0):
        print("\n Sorry! Product not available")
    elif (len(exist) != 0):
        csr.execute(f'''
            UPDATE Cart
            SET qty = qty + {qty}
            WHERE ProdID = {prodID} AND CustID = {custID}
        ''')
        print("\n Product successfully added to cart.")
    else:
        csr.execute(f"INSERT INTO Cart VALUES ({custID}, {prodID}, {qty})")
        print("\n Product successfully added to cart.")
    endFunction(csr, custID)

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
    endFunction(csr, custID)

def checkoutCart(csr, custID):
    os.system('cls')
    print()
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
        categ = getCustInfo(csr, custID)['Category']
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
    endFunction(csr, custID)

def viewOrders(csr, custID):
    os.system('cls')
    print()
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
    endFunction(csr, custID)

def changeCateg(csr, custID):
    os.system('cls')
    print(f"\n Choose from below:")
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
    oldCateg = getCustInfo(csr, custID)['Category']
    balance = getCustInfo(csr, custID)['WalletBalance']
    if oldCateg.lower() == newCateg.lower():
        print("\n Sorry! Same category")
    elif balance < cost:
        print("\n Sorry! Insufficient balance")
    else:
        csr.execute(f'''
            UPDATE Customers
            SET Category = '{newCateg}', WalletBalance = WalletBalance - {cost}
            WHERE CustID = '{custID}'
        ''')
        print(f"\n Changed successfully!\n\n Deducted an amount of Rs. {cost}.")
    endFunction(csr, custID)

def changeEmail(csr, custID):
    os.system('cls')
    oldEmail = input(f"\n  Current Email   : ")
    if (oldEmail != getCustInfo(csr, custID)['Email']):
        print("\n  Wrong email !!")
    else:
        newEmail = input(f"\n  New Email       : ")
        csr.execute(f'''
            UPDATE Customers
            SET Email = '{newEmail}'
            WHERE CustID = '{custID}'
        ''')
        print(f"\n  Email changed successfully!")
    endFunction(csr, custID)

def changePhone(csr, custID):
    os.system('cls')
    oldPhone = input(f"\n  Current Phone   : ")
    if (oldPhone != getCustInfo(csr, custID)['Phone']):
        print("\n  Wrong phone !!")
    else:
        newPhone = input(f"\n  New Phone       : ")
        csr.execute(f'''
            UPDATE Customers
            SET Phone = '{newPhone}'
            WHERE CustID = '{custID}'
        ''')
        print(f"\n  Phone changed successfully!")
    endFunction(csr, custID)

def changeAddress(csr, custID):
    os.system('cls')
    print("\n Enter new address")
    newHouse = input(f"\n  House       : ")
    newStreet = input(f"\n  Street      : ")
    newCity = input(f"\n  City        : ")
    csr.execute(f'''
        UPDATE Address
        SET House = '{newHouse}', Street = '{newStreet}', City = '{newCity}'
        WHERE CustID = '{custID}'
    ''')
    print(f"\n  Address changed successfully!")
    endFunction(csr, custID)

def changeUsername(csr, custID):
    os.system('cls')
    oldUsername = input(f"\n  Current Username   : ")
    if (oldUsername != getCustInfo(csr, custID)['Username']):
        print("\n  Wrong username !!")
    else:
        newUsername = input(f"\n  New Username       : ")
        csr.execute(f'''
            UPDATE Accounts
            SET Username = '{newUsername}'
            WHERE CustID = '{custID}'
        ''')
        print(f"\n  Username changed successfully!")
    endFunction(csr, custID)

def changePassword(csr, custID):
    os.system('cls')
    oldPassword = input(f"\n  Current Password   : ")
    if (oldPassword != getCustInfo(csr, custID)['Password']):
        print("\n  Wrong password !!")
    else:
        newPassword = input(f"\n  New Password       : ")
        csr.execute(f'''
            UPDATE Accounts
            SET Password = '{newPassword}'
            WHERE CustID = '{custID}'
        ''')
        print(f"\n  Password changed successfully!")
    endFunction(csr, custID)

def deactivate(csr, custID):
    os.system('cls')
    print()
    confirm = input("  Are you sure? (Y/N): ")
    print()
    if confirm.lower() != "y":
        print("  Deactivation canceled.")
        return endFunction(csr, custID)
    password = input("  Enter your password: ")
    print()
    getPassword = getCustInfo(csr, custID)['Password']
    if password != getPassword:
        print("  Wrong password. Account deactivation failed.")
        return endFunction(csr, custID)
    csr.execute(f'''
        DELETE FROM Customers
        WHERE CustID = {custID}
    ''')
    csr.execute('COMMIT')

    print("  Account deactivated successfully.")
    time.sleep(2)
    index.start(csr)
