DROP SCHEMA IF EXISTS Bumper_Bazaar;
CREATE SCHEMA Bumper_Bazaar;
USE Bumper_Bazaar;

--  Table structure for table Admin

    CREATE TABLE IF NOT EXISTS Admin (
        AdminID INT NOT NULL AUTO_INCREMENT,
        Password VARCHAR(30) NOT NULL,
        PRIMARY KEY (AdminID)
    );
    ALTER TABLE Admin AUTO_INCREMENT = 100001;

--  Table structure for table Customer

    CREATE TABLE IF NOT EXISTS Customers (
        CustID INT NOT NULL AUTO_INCREMENT,
        Name VARCHAR(50) NOT NULL,
        Gender ENUM('Male','Female') NOT NULL,
        Category ENUM('Normal','Prime','Elite') NOT NULL,
        Email VARCHAR(50),
        Phone CHAR(10),
        WalletBalance INT DEFAULT 0,
        PRIMARY KEY (CustID),
        CONSTRAINT BalCheck CHECK (WalletBalance >= 0)
    );
    ALTER TABLE Customers AUTO_INCREMENT = 1000;

--  Table structure for table Address

    CREATE TABLE IF NOT EXISTS Address (
        CustID INT NOT NULL AUTO_INCREMENT,
        House VARCHAR(50) NOT NULL,
        Street VARCHAR(50) NOT NULL,
        City VARCHAR(50) NOT NULL,
        PRIMARY KEY (CustID),
        FOREIGN KEY (CustID) REFERENCES Customers(CustID) ON DELETE CASCADE
    );
    ALTER TABLE Address AUTO_INCREMENT = 1000;

--  Table structure for table Account

    CREATE TABLE IF NOT EXISTS Accounts (
        CustID INT NOT NULL AUTO_INCREMENT,
        Username VARCHAR(30) NOT NULL,
        Password VARCHAR(30) NOT NULL,
        PRIMARY KEY (CustID, Username),
        FOREIGN KEY (CustID) REFERENCES Customers(CustID) ON DELETE CASCADE
    );
    ALTER TABLE Accounts AUTO_INCREMENT = 1000;

--  Table structure for table Inventory

    CREATE TABLE IF NOT EXISTS Inventory (
        ProdID INT NOT NULL AUTO_INCREMENT,
        ProdName VARCHAR(60) NOT NULL,
        Price INT,
        StockQty INT,
        PRIMARY KEY (ProdID),
        CONSTRAINT PriceCheck CHECK (Price > 0),
        CONSTRAINT StockCheck CHECK (StockQty >= 0)
    );
    ALTER TABLE Inventory AUTO_INCREMENT = 10000;

--  Table structure for table Cart

    CREATE TABLE IF NOT EXISTS Cart (
        CustID INT NOT NULL,
        ProdID INT NOT NULL,
        Qty INT,
        PRIMARY KEY (CustID, ProdID),
        FOREIGN KEY (CustID) REFERENCES Customers(CustID) ON DELETE CASCADE,
        FOREIGN KEY (ProdID) REFERENCES Inventory(ProdID) ON DELETE CASCADE,
        CONSTRAINT QtyCheck CHECK (Qty > 0)
    );

--  Table structure for table Orders

    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INT NOT NULL AUTO_INCREMENT,
        CustID INT NOT NULL,
        PayMode ENUM('Cash','Wallet') NOT NULL,
        Amount INT NOT NULL,
        Status ENUM('Placed','Shipped','Delivered') NOT NULL,
        PRIMARY KEY (OrderID),
        FOREIGN KEY (CustID) REFERENCES Cart(CustID) ON DELETE CASCADE
    );
    ALTER TABLE Orders AUTO_INCREMENT = 1000000;