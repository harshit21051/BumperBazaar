import index, os, time
from customer.custMenuFunc import *

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
    name = input("\n  Name       : ")
    gender = input("\n  Gender     : ")
    email = input("\n  Email      : ")
    phone = input("\n  Phone      : ")

    csr.execute(f'''
        INSERT INTO Customers
        (Name, Gender, Category, Email, Phone, WalletBalance)
        VALUES
        ('{name}', '{gender}', 'Normal', '{email}', '{phone}', 0)
    ''')

    # Get the CustID of the inserted customer
    cust_id = csr.lastrowid

    # Insert data into the Address table
    print("\n  Address")
    house = input("\n    House    : ")
    street = input("\n    Street   : ")
    city = input("\n    City     : ")

    csr.execute(f'''
        INSERT INTO Address
        (CustID, House, Street, City)
        VALUES
        ({cust_id}, '{house}', '{street}', '{city}')
    ''')

    # Insert data into the Accounts table
    print("\n  Account")
    username = input("\n    Username : ")
    password = input("\n    Password : ")

    csr.execute(f'''
        SELECT * FROM Accounts
        WHERE Username = '{username}'
    ''')
    exist = csr.fetchone()
    if exist is not None:
        print("\n  Email already exists!")
    else:
        csr.execute(f'''
            INSERT INTO Accounts
            (CustID, Username, Password)
            VALUES
            ({cust_id}, '{username}', '{password}')
        ''')

        print("\n  Registered successfully!!")
        csr.execute("COMMIT")
    time.sleep(2)
    custLogin(csr)

def custMenu(csr, custID):
    name = getCustInfo(csr, custID)['Name']
    print(f" Welcome {name} !!")
    print()
    print("   1)  Browse products")
    print("   2)  Search for product")
    print("   3)  View cart")
    print("   4)  Add to cart")
    print("   5)  Empty cart")
    print("   6)  Checkout cart")
    print("   7)  View orders")
    print("   8)  View profile")
    print("   9)  Add amount to wallet")
    print("   10) Change category")
    print("   11) Change email")
    print("   12) Change phone")
    print("   13) Change address")
    print("   14) Change username")
    print("   15) Change password")
    print("   16) Deactivate account")
    print("   17) Logout")
    print()
    opt = int(input(" Enter option : "))
    index.printformat()
    if (opt == 1):
        return browseProd(csr, custID)
    elif (opt == 2):
        return searchProd(csr, custID)
    elif (opt == 3):
        return viewCart(csr, custID)
    elif (opt == 4):
        return addCart(csr, custID)
    elif (opt == 5):
        return emptyCart(csr, custID)
    elif (opt == 6):
        return checkoutCart(csr, custID)
    elif (opt == 7):
        return viewOrders(csr, custID)
    elif (opt == 8):
        return profile(csr, custID)
    elif (opt == 9):
        return addAmt(csr, custID)
    elif (opt == 10):
        return changeCateg(csr, custID)
    elif (opt == 11):
        return changeEmail(csr, custID)
    elif (opt == 12):
        return changePhone(csr, custID)
    elif (opt == 13):
        return changeAddress(csr, custID)
    elif (opt == 14):
        return changeUsername(csr, custID)
    elif (opt == 15):
        return changePassword(csr, custID)
    elif (opt == 16):
        return deactivate(csr, custID)
    else:
        return index.start(csr)
