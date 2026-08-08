import pandas as pd

# Load CSV files
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

print("Files Loaded Successfully!\n")

# -----------------------------
# Clean Customers
# -----------------------------

customers["email"] = customers["email"].replace("invalid_email", "unknown@email.com")

customers.to_csv("data/customers_cleaned.csv", index=False)

print("customers_cleaned.csv created")

# -----------------------------
# Clean Products
# -----------------------------

products["product_name"] = (
    products["product_name"]
    .str.strip()
    .str.title()
)

products.to_csv("data/products_cleaned.csv", index=False)

print("products_cleaned.csv created")

# -----------------------------
# Clean Orders
# -----------------------------

orders["customer_id"] = orders["customer_id"].fillna(0)

orders.to_csv("data/orders_cleaned.csv", index=False)

print("orders_cleaned.csv created")

# -----------------------------
# Clean Order Items
# -----------------------------

order_items.loc[order_items["quantity"] < 0, "quantity"] = 1

order_items.to_csv("data/order_items_cleaned.csv", index=False)

print("order_items_cleaned.csv created")

print("\nData Cleaning Completed Successfully!")