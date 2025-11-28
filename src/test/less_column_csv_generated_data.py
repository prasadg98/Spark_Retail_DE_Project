import os
import csv
import random
from datetime import datetime

# Customers, Stores, Products, Salespersons
customer_ids = list(range(1, 501))  # 500 customers
store_ids = list(range(101, 106))   # 5 stores

# U.S. products with reasonable USD prices
product_data = {
    "Quaker Oats": 3.5,
    "Sugar": 2.0,
    "All-purpose Flour": 1.8,
    "Besan": 2.2,
    "Refined Oil": 4.0,
    "Clinic Plus Shampoo": 5.0,
    "Dant Kanti Toothpaste": 3.0,
    "Nutrella": 2.5,
    "Coca Cola": 1.5,
    "Pepsi": 1.5,
    "Lay's Chips": 2.0,
    "Kellogg's Cornflakes": 4.5,
    "Oreo": 3.0,
    "Cadbury Chocolate": 2.5,
    "Red Bull": 3.0,
    "Milo": 4.0,
    "Nescafe Coffee": 5.0,
    "Kraft Cheese": 3.5,
    "Doritos": 2.5,
    "Heinz Ketchup": 3.0
}

# 10 salespersons per store, IDs unique per store
sales_persons = {store_id: list(range(store_id * 10, store_id * 10 + 10)) for store_id in store_ids}

# File location
file_location = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data"
os.makedirs(file_location, exist_ok=True)

# Input date
input_date_str = input("Enter the date for which you want to generate (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

# CSV file path
csv_file_path = os.path.join(file_location, f"sales_data_{input_date_str}.csv")

with open(csv_file_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Keep original column names and order
    csvwriter.writerow([
        "customer_id", "product_name", "sales_date", "sales_person_id",
        "price", "quantity", "total_cost", "payment_mode"
    ])

    for _ in range(1000):  # Number of rows
        customer_id = random.choice(customer_ids)
        store_id = random.choice(store_ids)
        product_name = random.choice(list(product_data.keys()))
        sales_date = input_date
        sales_person_id = random.choice(sales_persons[store_id])
        quantity = random.randint(1, 10)
        price = product_data[product_name]
        total_cost = round(price * quantity, 2)
        payment_mode = random.choice(["cash", "card", "UPI", "credit"])

        csvwriter.writerow([
            customer_id, product_name, sales_date.strftime("%Y-%m-%d"),
            sales_person_id, price, quantity, total_cost, payment_mode
        ])

print("CSV file generated successfully:", csv_file_path)
