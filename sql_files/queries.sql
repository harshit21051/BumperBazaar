USE Bumper_Bazaar;

-- 1) Some basic queries

    SELECT * FROM Admin;
    DESC Admin;
    SHOW CREATE TABLE Admin;

    SELECT * FROM Customers;
    DESC Customers;
    SHOW CREATE TABLE Customers;

    SELECT * FROM Address;
    DESC Address;
    SHOW CREATE TABLE Address;

    SELECT * FROM Accounts;
    DESC Accounts;
    SHOW CREATE TABLE Accounts;

    SELECT * FROM Inventory;
    DESC Inventory;
    SHOW CREATE TABLE Inventory;

    SELECT * FROM Cart;
    DESC Cart;
    SHOW CREATE TABLE Cart;

    SELECT * FROM Payments;
    DESC Payments;
    SHOW CREATE TABLE Payments;

    SELECT * FROM Orders;
    DESC Orders;
    SHOW CREATE TABLE Orders;


-- 2) Show the number of rows in each table of this database

    SELECT table_name AS `Table name`, table_rows AS `No. of items`
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'Bumper_Bazaar';


-- 3) Show the relationship among tables

    SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME,
    REFERENCED_COLUMN_NAME, REFERENCED_TABLE_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE TABLE_SCHEMA = 'Bumper_Bazaar';


-- 4) Show all the constraints in this database
    SELECT TABLE_NAME, CONSTRAINT_TYPE, CONSTRAINT_NAME
    FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
    WHERE TABLE_SCHEMA = 'Bumper_Bazaar';


-- 5) Show all customer details along with their account details

    SELECT *
    FROM Customers C
    INNER JOIN Accounts A
    ON C.CustID = A.CustID;


-- 6) Show all customer details along with their addresses and account details in the order of their categories

    SELECT
    CustID, Name, Gender, Category, Email, Phone, WalletBalance,
    Concat(House,', ',Street,', ',City) AS Address,
    Username, Password 
    FROM Customers
    NATURAL JOIN Address
    NATURAL JOIN Accounts
    ORDER BY Category;


-- 7) Show the cart details of each customer

    SELECT *
    FROM Customers
    NATURAL JOIN Inventory
    NATURAL JOIN Cart;


-- 8) Show the customers with maximum number of items in their cart

    SELECT CustID, Name AS `Customer Name`,
    count(ProdID) AS `No of items`,
    sum(Price) AS `Total Cart Amount`
    FROM Customers
    NATURAL JOIN Inventory
    NATURAL JOIN Cart
    GROUP BY CustID
    HAVING count(ProdID) >= ALL (
        SELECT count(ProdID)
        FROM Customers
        NATURAL JOIN Inventory
        NATURAL JOIN Cart
        GROUP BY CustID
    );


-- 9) Show the customers with 2 items in their cart in descending order of their names

    SELECT CustID, Name AS `Customer Name`,
    count(ProdID) AS `No of items`,
    sum(Price) AS `Total Cart Amount`
    FROM Customers
    NATURAL JOIN Inventory
    NATURAL JOIN Cart
    GROUP BY CustID
    HAVING count(ProdID) = 2
    ORDER BY `Customer Name` DESC;


-- 10) Show the customers with lowest and highest wallet balance

    SELECT * FROM Customers
    WHERE WalletBalance <= ALL( -- Minimum wallet balance
        SELECT WalletBalance
        FROM Customers
    )
    OR WalletBalance >= ALL(    -- Maximum wallet balance
        SELECT WalletBalance
        FROM Customers
    );


-- 11) Show the cheapest and the most expensive product of the inventory

    SELECT * FROM Inventory
    WHERE Price <= ALL( -- Minimum price
        SELECT Price
        FROM Inventory
    )
    OR Price >= ALL(    -- Maximum price
        SELECT Price
        FROM Inventory
    );


-- 12) Show the products whose price is greater than price of 'Stock - Veal, Brown'

    SELECT I.ProdID, I.ProdName, I.Price, I.StockQty
    FROM Inventory AS I, Inventory AS J
    WHERE I.Price > J.Price
    AND J.ProdName = 'Stock - Veal, Brown';


-- 13) Show the payment mode of customers

    SELECT *
    FROM Customers
    NATURAL JOIN Payments
    NATURAL JOIN Orders;


-- 14) Show the details of each item in the cart of customer Erny Dubois

    SELECT ProdID, ProdName, Price, Qty
    FROM Cart
    NATURAL JOIN Inventory
    WHERE CustID IN(
        SELECT CustID
        FROM Customers
        WHERE lower(Name) = 'erny dubois'
    );


-- 15) Show the amount invested by the shop on products like wine

    SELECT sum(Price*StockQty)
    FROM Inventory
    WHERE upper(ProdName) like "%WINE%";


-- 16) Show all the female elite and prime customers

    SELECT *
    FROM Customers
    WHERE lower(Gender) = 'female'
    AND lower(Category) in ('prime','elite');


-- 17) Show the union of all normal and elite customers

    (SELECT *
    FROM Customers
    WHERE lower(Category) = 'normal')
    UNION
    (SELECT *
    FROM Customers
    WHERE lower(Category) = 'elite');


-- 18) Show all customers who are government employees

    SELECT *
    FROM Customers
    WHERE Email like "%gov%";


-- 19) Update the name and email of customer 'Aldridge Newlove'

    UPDATE Customers
    SET
    Name = 'Ashok Kumar',
    Email = 'ashokct2003@hotmail.com'
    WHERE Name = 'Aldridge Newlove';

    SELECT * FROM Customers
    ORDER BY Name;


-- 20) Update the price and stock quantity of item 'Chicken - Soup Base'

    UPDATE Inventory
    SET
    Price = 315,
    StockQty = 1500
    WHERE ProdName = 'Chicken - Soup Base';

    SELECT * FROM Inventory
    ORDER BY ProdName;


-- 21) Update the city of Customer 'Sapphira Massen'

    UPDATE Address
    SET City = 'Patna'
    WHERE CustID IN (
        SELECT CustID
        FROM Customers
        WHERE Name = 'Sapphira Massen'
    );

    SELECT
    CustID, Name, Email, Phone,
    Concat(House,', ',Street,', ',City) AS Address
    FROM Customers
    NATURAL JOIN Address
    ORDER BY Name;


-- 22) Delete the column Gender from Customers

    ALTER TABLE Customers
    DROP COLUMN Gender;

    SELECT * FROM Customers
    ORDER BY Name;


-- 23) Delete the column Street from Address

    ALTER TABLE Address
    DROP COLUMN Street;

    SELECT * FROM Address;