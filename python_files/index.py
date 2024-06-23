import mysql.connector as sqlp
import os, time
import admin.adminLogin as admin
import customer.custLogin as customer

def printformat():
    print("\n-------------------------------------------------------------------------------\n")

def start(csr):
    os.system('cls')
    print("-+---------------------------------------------------------------------------+-")
    print(" -----------------------------+- BUMPER BAZAAR -+----------------------------- ")
    print("-+---------------------------------------------------------------------------+-")
    print()
    print("   1) Enter as admin")
    print("   2) Enter as customer")
    print("   3) Exit")
    print()
    opt = int(input(" Enter option : "))
    if (opt == 1):
        return admin.adminLogin(csr)
    elif (opt == 2):
        return customer.custLogin(csr)
    else:
        print("\n Thank you and visit again.")
        printformat()
        time.sleep(0.6)
        exit()

if __name__ == "__main__":
    mydb = sqlp.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "Bumper_Bazaar"
    )
    csr = mydb.cursor()
    start(csr)
