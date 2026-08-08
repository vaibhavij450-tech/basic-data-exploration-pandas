import sqlite3
import pandas as pd

conn = sqlite3.connect("database/ecommerce.db")

customers = pd.read_csv("data/customers_cleaned.csv")
products = pd.read_csv("data/products_cleaned.csv")
orders = pd.read_csv("data/orders_cleaned.csv")
order_items = pd.read_csv("data/order_items_cleaned.csv")

customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")