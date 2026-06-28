-- SQL Superstore Analysis

USE superstoredb;

-- Show all tables
SHOW TABLES;

-- Display all records
SELECT *
FROM `sample - superstore`;

-- Count rows
SELECT COUNT(*) AS TotalRows
FROM `sample - superstore`;

-- Display table structure
DESCRIBE `sample - superstore`;

-- Query 5: Sales greater than 1000
SELECT *
FROM `sample - superstore`
WHERE Sales > 1000;

-- Query 6: Furniture Category
SELECT *
FROM `sample - superstore`
WHERE Category='Furniture';

-- Query 7: Technology Category
SELECT *
FROM `sample - superstore`
WHERE Category='Technology';

-- Query 8: West Region
SELECT *
FROM `sample - superstore`
WHERE Region='West';

-- Query 9: Profit greater than 500
SELECT *
FROM `sample - superstore`
WHERE Profit>500;

-- Query 10: Total Sales by Region
SELECT Region,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY Region;

-- Query 11: Average Sales by Category
SELECT Category,
AVG(Sales) AS AverageSales
FROM `sample - superstore`
GROUP BY Category;

-- Query 12: Total Quantity Sold by Category
SELECT Category,
SUM(Quantity) AS TotalQuantity
FROM `sample - superstore`
GROUP BY Category;

-- Query 13: Total Profit by Region
SELECT Region,
SUM(Profit) AS TotalProfit
FROM `sample - superstore`
GROUP BY Region;

-- Query 14: Number of Orders by Ship Mode
SELECT `Ship Mode`,
COUNT(*) AS TotalOrders
FROM `sample - superstore`
GROUP BY `Ship Mode`;

-- Query 15: Top 10 Customers by Sales
SELECT `Customer Name`,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY `Customer Name`
ORDER BY TotalSales DESC
LIMIT 10;

-- Query 16: Top 10 Products by Sales
SELECT `Product Name`,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY `Product Name`
ORDER BY TotalSales DESC
LIMIT 10;

-- Query 17: Top 10 Cities by Sales
SELECT City,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY City
ORDER BY TotalSales DESC
LIMIT 10;

-- Query 18: Top 10 States by Sales
SELECT State,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY State
ORDER BY TotalSales DESC
LIMIT 10;

-- Query 19: Top 10 Sub-Categories by Profit
SELECT `Sub-Category`,
SUM(Profit) AS TotalProfit
FROM `sample - superstore`
GROUP BY `Sub-Category`
ORDER BY TotalProfit DESC
LIMIT 10;

-- Query 20: Monthly Sales Trend
SELECT
YEAR(STR_TO_DATE(`Order Date`, '%m/%d/%Y')) AS Year,
MONTH(STR_TO_DATE(`Order Date`, '%m/%d/%Y')) AS Month,
SUM(Sales) AS MonthlySales
FROM `sample - superstore`
GROUP BY Year, Month
ORDER BY Year, Month;

-- Query 21: Region-wise Average Profit
SELECT Region,
AVG(Profit) AS AverageProfit
FROM `sample - superstore`
GROUP BY Region;

-- Query 22: Duplicate Order IDs
SELECT `Order ID`,
COUNT(*) AS DuplicateCount
FROM `sample - superstore`
GROUP BY `Order ID`
HAVING COUNT(*) > 1;

-- Query 23: Missing Values Check
SELECT
COUNT(*) AS TotalRows,
COUNT(Sales) AS SalesRows,
COUNT(Profit) AS ProfitRows,
COUNT(`Customer Name`) AS CustomerRows
FROM `sample - superstore`;

-- Query 24: Highest Profit Product
SELECT `Product Name`,
SUM(Profit) AS TotalProfit
FROM `sample - superstore`
GROUP BY `Product Name`
ORDER BY TotalProfit DESC
LIMIT 10;

-- Query 25: Segment-wise Sales
SELECT Segment,
SUM(Sales) AS TotalSales
FROM `sample - superstore`
GROUP BY Segment;