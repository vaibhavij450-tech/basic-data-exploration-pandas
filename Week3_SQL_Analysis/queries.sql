-- ============================================================
-- Week 3 - SQL Assignment
-- Name: Vaibhavi Jain
-- Dataset: Superstore
-- ============================================================

USE superstoredb;

-- ============================================================
-- STEP 1: Create superstore_raw
-- ============================================================

DROP TABLE IF EXISTS superstore_raw;

CREATE TABLE superstore_raw AS
SELECT *
FROM `sample - superstore`;

SELECT * FROM superstore_raw LIMIT 10;

-- ============================================================
-- STEP 2: Create Customers Table
-- ============================================================

DROP TABLE IF EXISTS customers;

CREATE TABLE customers AS
SELECT DISTINCT
    `Customer ID`,
    `Customer Name`,
    Segment
FROM superstore_raw;

SELECT * FROM customers LIMIT 10;

-- ============================================================
-- STEP 3: Create Orders Table
-- ============================================================

DROP TABLE IF EXISTS orders;

CREATE TABLE orders AS
SELECT DISTINCT
    `Order ID`,
    `Order Date`,
    `Ship Date`,
    `Ship Mode`,
    `Customer ID`,
    Sales,
    Quantity,
    Discount,
    Profit
FROM superstore_raw;

SELECT * FROM orders LIMIT 10;

-- ============================================================
-- STEP 4: Create Products Table
-- ============================================================

DROP TABLE IF EXISTS products;

CREATE TABLE products AS
SELECT DISTINCT
    `Product ID`,
    `Product Name`,
    Category,
    `Sub-Category`
FROM superstore_raw;

SELECT * FROM products LIMIT 10;

-- ============================================================
-- Show Tables
-- ============================================================

SHOW TABLES;

-- ============================================================
-- Query 1
-- Customers with Above Average Sales (Subquery)
-- ============================================================

SELECT *
FROM orders
WHERE Sales >
(
    SELECT AVG(Sales)
    FROM orders
);

-- ============================================================
-- Query 2
-- Highest Order for Each Customer (Subquery)
-- ============================================================

SELECT *
FROM orders o
WHERE Sales =
(
    SELECT MAX(Sales)
    FROM orders
    WHERE `Customer ID` = o.`Customer ID`
);

-- ============================================================
-- Query 3
-- Total Sales Per Customer (CTE)
-- ============================================================

WITH CustomerSales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS TotalSales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *
FROM CustomerSales;

-- ============================================================
-- Query 4
-- Customers Above Average Total Sales
-- ============================================================

WITH CustomerSales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS TotalSales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *
FROM CustomerSales
WHERE TotalSales >
(
    SELECT AVG(TotalSales)
    FROM CustomerSales
);

-- ============================================================
-- Query 5
-- Customer Ranking (Window Function)
-- ============================================================

WITH CustomerSales AS
(
    SELECT
        `Customer ID`,
        SUM(Sales) AS TotalSales
    FROM orders
    GROUP BY `Customer ID`
)

SELECT *,
RANK() OVER(ORDER BY TotalSales DESC) AS CustomerRank
FROM CustomerSales;

-- ============================================================
-- Query 6
-- Row Number per Customer
-- ============================================================

SELECT
`Customer ID`,
`Order ID`,
Sales,

ROW_NUMBER() OVER
(
PARTITION BY `Customer ID`
ORDER BY Sales DESC
)
AS RowNum

FROM orders;

-- ============================================================
-- Query 7
-- Final Query using JOIN + CTE + Window Function
-- ============================================================

WITH CustomerSales AS
(
SELECT
`Customer ID`,
SUM(Sales) AS TotalSales

FROM orders

GROUP BY `Customer ID`
)

SELECT

c.`Customer Name`,
cs.TotalSales,

RANK() OVER
(
ORDER BY cs.TotalSales DESC
)
AS CustomerRank

FROM customers c

JOIN CustomerSales cs

ON c.`Customer ID` = cs.`Customer ID`;

-- ============================================================
-- MINI PROJECT
-- ============================================================

-- Top 5 Customers

WITH CustomerSales AS
(
SELECT
`Customer ID`,
SUM(Sales) AS TotalSales

FROM orders

GROUP BY `Customer ID`
)

SELECT

c.`Customer Name`,
cs.TotalSales

FROM customers c

JOIN CustomerSales cs

ON c.`Customer ID` = cs.`Customer ID`

ORDER BY TotalSales DESC

LIMIT 5;

-- Bottom 5 Customers

WITH CustomerSales AS
(
SELECT
`Customer ID`,
SUM(Sales) AS TotalSales

FROM orders

GROUP BY `Customer ID`
)

SELECT

c.`Customer Name`,
cs.TotalSales

FROM customers c

JOIN CustomerSales cs

ON c.`Customer ID` = cs.`Customer ID`

ORDER BY TotalSales ASC

LIMIT 5;

-- Customers with Only One Order

SELECT
`Customer ID`,
COUNT(*) AS OrdersCount

FROM orders

GROUP BY `Customer ID`

HAVING COUNT(*) = 1;

-- Customers Above Average Total Sales

WITH CustomerSales AS
(
SELECT
`Customer ID`,
SUM(Sales) AS TotalSales

FROM orders

GROUP BY `Customer ID`
)

SELECT *

FROM CustomerSales

WHERE TotalSales >
(
SELECT AVG(TotalSales)

FROM CustomerSales
);

-- Highest Order Value Per Customer

SELECT
`Customer ID`,
MAX(Sales) AS HighestOrder

FROM orders

GROUP BY `Customer ID`;