import os
import csv
import random
from datetime import datetime

# Customers, Stores, Products, Salespersons
customer_ids = list(range(1, 501))  # 500 customers
store_ids = list(range(101, 106))  # 5 stores

# Example American products with reasonable USD prices
product_data = {
    "Quaker Oats": 3.5,
    "Coca Cola": 1.2,
    "Peanut Butter": 4.0,
    "Cheerios": 3.8,
    "Doritos": 2.5,
    "Campbell Soup": 2.0,
    "Nutella": 5.0,
    "Hershey Chocolate": 2.8,
    "Kellogg's Corn Flakes": 3.2,
    "Gatorade": 1.5
}

# 10 salespersons per store
sales_persons = {store_id: list(range(store_id * 10 + 1, store_id * 10 + 11)) for store_id in store_ids}

# File location
file_location = "C:\\Users\\mahakal.s\\Documents\\Retail_Project_Data\\sales_data_to_s3\\"
os.makedirs(file_location, exist_ok=True)

# Input date
input_date_str = input("Enter the date for which you want to generate (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, "%Y-%m-%d")

# CSV file path
csv_file_path = os.path.join(file_location, f"sales_data_{input_date_str}.csv")

with open(csv_file_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    # Keep original schema and column order
    csvwriter.writerow([
        "customer_id", "store_id", "product_name", "sales_date",
        "sales_person_id", "price", "quantity", "total_cost", "payment_mode"
    ])

    for _ in range(1000):
        customer_id = random.choice(customer_ids)
        store_id = random.choice(store_ids)
        product_name = random.choice(list(product_data.keys()))
        sales_date = input_date
        sales_person_id = random.choice(sales_persons[store_id])
        quantity = random.randint(1, 10)
        price = product_data[product_name]
        total_cost = price * quantity
        payment_mode = random.choice(["cash", "card", "UPI", "credit"])

        csvwriter.writerow([
            customer_id, store_id, product_name, sales_date.strftime("%Y-%m-%d"),
            sales_person_id, price, quantity, total_cost, payment_mode
        ])

print("CSV file generated successfully:", csv_file_path)
