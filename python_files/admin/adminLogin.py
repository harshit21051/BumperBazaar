import index, os, time
from admin.adminMenuFunc import *

def adminLogin(csr):
    os.system('cls')
    print("\n Administrator login\n")
    adminID = int(input("   Admin ID : "))
    print()
    pw = input("   Password : ")
    csr.execute(f'''
        SELECT * FROM Admin
        WHERE AdminID = {adminID}
        AND Password = '{pw}'
    ''')
    login = csr.fetchall()
    if (len(login) == 0):
        print("\n   Incorrect login !!")
        index.printformat()
        time.sleep(2)
        index.start(csr)
    else:
        os.system('cls')
        print()
        adminMenu(csr, adminID)

def adminMenu(csr, adminID):
    print(f" Welcome Administrator !!")
    print()
    print("   1)  View inventory")
    print("   2)  Add to inventory")
    print("   3)  Remove from inventory")
    print("   4)  Update stock")
    print("   5)  Update price")
    print("   6)  View customer details")
    print("   7)  View orders")
    print("   8)  Change order status")
    print("   9)  View account statement")
    print("   10) Logout")
    print()
    opt = int(input(" Enter option : "))
    index.printformat()
    if (opt == 1):
        return viewInv(csr, adminID)
    elif (opt == 2):
        return addInv(csr, adminID)
    elif (opt == 3):
        return remInv(csr, adminID)
    elif (opt == 4):
        return updStock(csr, adminID)
    elif (opt == 5):
        return updPrice(csr, adminID)
    elif (opt == 6):
        return viewCust(csr, adminID)
    elif (opt == 7):
        return viewOrders(csr, adminID)
    elif (opt == 8):
        return changeOrderStatus(csr, adminID)
    elif (opt == 9):
        return viewAccStmt(csr, adminID)
    else:
        return index.start(csr)
