import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

queries = {
    "Total Customers":
    "SELECT COUNT(*) AS total_customers FROM customers;",

    "Total Products":
    "SELECT COUNT(*) AS total_products FROM products;",

    "Total Orders":
    "SELECT COUNT(*) AS total_orders FROM orders;",

    "Top 5 Expensive Products":
    """
    SELECT product_name, price
    FROM products
    ORDER BY price DESC
    LIMIT 5;
    """,

    "Orders per Customer":
    """
    SELECT customer_id, COUNT(*) AS total_orders
    FROM orders
    GROUP BY customer_id
    ORDER BY total_orders DESC
    LIMIT 10;
    """
}

for title, sql in queries.items():
    print("\n" + "="*50)
    print(title)
    print("="*50)
    df = pd.read_sql_query(sql, conn)
    print(df)

conn.close()