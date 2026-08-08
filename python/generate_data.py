import pandas as pd
from faker import Faker
import random
import os

# Create Faker object
fake = Faker()

# Create a list to store customer data
customers = []

# Generate 500 customers
for i in range(1, 501):
    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
       "email": fake.email() if random.random() > 0.02 else "invalid_email",
        "city": fake.city(),
        "country": fake.country()
    })

# Create DataFrame
customers_df = pd.DataFrame(customers)


customers_df.to_csv("data/customers.csv", index=False)

print("customers.csv created successfully!")
print("Saved to: data/customers.csv")
print(customers_df.head())

# -------------------------------
# Generate Products Data
# -------------------------------

products = []

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

for i in range(1, 501):
    products.append({
        "product_id": i,
       "product_name": random.choice([
    fake.word().title(),
    "  laptop  ",
    "PHONE",
    " book "
]),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 5000), 2)
    })

products_df = pd.DataFrame(products)

products_df.to_csv("data/products.csv", index=False)

print("\nproducts.csv created successfully!")
print(products_df.head())
# -------------------------------
# Generate Orders Data (with issues)
# -------------------------------

orders = []

for i in range(1, 501):

    # Introduce some missing customer IDs
    customer = random.randint(1, 500)
    if random.random() < 0.02:      # About 2% missing
        customer = None

    # Introduce one incorrect date format occasionally
    order_date = fake.date_between(start_date="-2y", end_date="today")
    if random.random() < 0.02:
        order_date = "32/13/2025"

    orders.append({
        "order_id": i,
        "customer_id": customer,
        "order_date": order_date,
        "status": random.choice(["Delivered", "Pending", "Cancelled"])
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv("data/orders.csv", index=False)

print("orders.csv created successfully!")
# -------------------------------
# Generate Order Items (with issues)
# -------------------------------

order_items = []

for i in range(1, 501):

    quantity = random.randint(1, 5)

    # Introduce negative quantities
    if random.random() < 0.02:
        quantity = -2

    price = round(random.uniform(100, 5000), 2)

    order_items.append({
        "order_item_id": i,
        "order_id": random.randint(1, 500),
        "product_id": random.randint(1, 500),
        "quantity": quantity,
        "price": price
    })

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv("data/order_items.csv", index=False)

print("order_items.csv created successfully!")