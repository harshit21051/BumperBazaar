import index, os, time
from customer.custMenuFunc import *

def getCustName(csr, custID):
    csr.execute(f'''
        SELECT Name FROM Customers
        WHERE CustID = {custID}
    ''')
    nameStr = csr.fetchall()
    for i in nameStr:
        for x in i:
            name = x
    return name

def custLogin(csr):
    os.system('cls')
    print(f"\n Choose from below:")
    print()
    print("   1) Login")
    print("   2) Sign up")
    print("   3) Back")
    print()
    opt = int(input(" Enter option : "))
    if (opt == 1):
        login(csr)
    elif (opt == 2):
        signup(csr)
    else:
        index.start(csr)

def login(csr):
    os.system('cls')
    print("\n Customer login\n")
    un = input("   Username : ")
    pw = input("\n   Password : ")
    csr.execute(f'''
        SELECT * FROM Accounts
        WHERE Username = '{un}'
        AND Password = '{pw}'
    ''')
    login = csr.fetchall()
    if (len(login) == 0):
        print("\n   Incorrect login !!")
        index.printformat()
        time.sleep(2)
        index.start(csr)
    else:
        csr.execute(f'''
            SELECT CustID FROM Customers
            WHERE CustID IN (
                SELECT CustID FROM Accounts
                WHERE Username = '{un}'
                AND Password = '{pw}'
            )
        ''')
        idStr = csr.fetchall()
        for i in idStr:
            for x in i:
                custID = int(x)
        os.system('cls')
        print()
        custMenu(csr, custID)

def signup(csr):
    os.system('cls')
    print("\n Customer sign up\n")
    name = input("\n  Name: ")
    gender = input("\n  Gender (Male/Female): ")
    email = input("\n  Email: ")
    phone = input("\n  Phone: ")

    csr.execute(f'''
        INSERT INTO Customers
        (Name, Gender, Category, Email, Phone, WalletBalance)
        VALUES
        ('{name}', '{gender}', 'Normal', '{email}', '{phone}', 0)
    ''')

    # Get the CustID of the inserted customer
    cust_id = csr.lastrowid

    # Insert data into the Address table
    print("\n  Address:")
    house = input("\n    House: ")
    street = input("\n    Street: ")
    city = input("\n    City: ")

    csr.execute(f'''
        INSERT INTO Address
        (CustID, House, Street, City)
        VALUES
        ({cust_id}, '{house}', '{street}', '{city}')
    ''')

    # Insert data into the Accounts table
    print("\n  Account:")
    username = input("\n    Username: ")
    password = input("\n    Password: ")

    csr.execute(f'''
        INSERT INTO Accounts
        (CustID, Username, Password)
        VALUES
        ({cust_id}, '{username}', '{password}')
    ''')

    print("  Registered successfully!!")
    csr.execute("COMMIT")
    custLogin(csr)

def custMenu(csr, custID):
    name = getCustName(csr, custID)
    print(f" Welcome {name} !!")
    print()
    print("   1)  Browse products")
    print("   2)  View cart")
    print("   3)  View profile")
    print("   4)  Add amount to wallet")
    print("   5)  Add to cart")
    print("   6)  Empty cart")
    print("   7)  Checkout cart")
    print("   8)  View orders")
    print("   9)  Change category")
    print("   10) Logout")
    print()
    opt = int(input(" Enter option : "))
    index.printformat()
    if (opt == 1):
        return browseProd(csr, custID)
    elif (opt == 2):
        return viewCart(csr, custID)
    elif (opt == 3):
        return profile(csr, custID)
    elif (opt == 4):
        return addAmt(csr, custID)
    elif (opt == 5):
        return addCart(csr, custID)
    elif (opt == 6):
        return emptyCart(csr, custID)
    elif (opt == 7):
        return checkoutCart(csr, custID)
    elif (opt == 8):
        return viewOrders(csr, custID)
    elif (opt == 9):
        return changeCateg(csr, custID)
    else:
        return index.start(csr)
