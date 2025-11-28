import csv
import os
import random
from datetime import datetime, timedelta

# 500 customers
customer_ids = list(range(1, 501))

# 5 stores (IDs 201–205)
store_ids = list(range(201, 206))

# American products with realistic USD prices
product_data = {
    # Groceries
    "Coca-Cola 12oz Can": 1.25,
    "Pepsi 12oz Can": 1.25,
    "Lay's Classic Chips 8oz": 3.49,
    "Doritos Nacho Cheese 9.75oz": 4.29,
    "Kellogg's Corn Flakes 18oz": 4.25,
    "Cheerios 18oz": 4.99,
    "Quaker Oats 42oz": 5.79,
    "Jif Peanut Butter 16oz": 3.99,
    "Smucker’s Strawberry Jam 20oz": 3.89,
    "Nature Valley Granola Bars (Box of 6)": 4.49,
    "Hershey's Milk Chocolate Bar": 1.50,
    "Ben & Jerry’s Ice Cream Pint": 5.99,
    "Tostitos Salsa 15.5oz": 3.99,
    "Kraft Mac & Cheese Box": 1.39,
    "Heinz Ketchup 20oz": 2.75,
    "Hunt’s Tomato Sauce 15oz": 1.25,
    "Del Monte Pineapple Chunks 20oz": 2.19,
    "Campbell’s Chicken Noodle Soup 10.5oz": 2.49,
    "Starbucks Cold Brew Bottle 11oz": 3.99,
    "Nestlé Toll House Chocolate Chips 12oz": 3.89,

    # Household items
    "Tide Laundry Detergent 92oz": 13.99,
    "Downy Fabric Softener 51oz": 6.49,
    "Bounty Paper Towels (6 Rolls)": 11.99,
    "Charmin Ultra Soft Toilet Paper (12 Rolls)": 14.99,
    "Dawn Dish Soap 19oz": 3.49,
    "Clorox Disinfecting Wipes (75 Count)": 6.29,
    "Glad Trash Bags (40 Count)": 8.99,
    "Ziploc Storage Bags (Quart, 50 Count)": 5.49,

    # Personal care
    "Colgate Toothpaste 6oz": 3.25,
    "Crest 3D White Toothpaste 4.1oz": 3.79,
    "Dove Body Wash 22oz": 6.49,
    "Head & Shoulders Shampoo 13.5oz": 6.99,
    "Pantene Conditioner 12oz": 5.79,
    "Old Spice Deodorant": 5.29,
    "Gillette Razor 3-Pack": 9.99,
    "Neutrogena Facial Cleanser 6oz": 7.49,
    "Aveeno Daily Moisturizing Lotion 12oz": 8.49,
    "Irish Spring Bar Soap 6-Pack": 5.99
}

# 10 salespersons per store
sales_persons = {store_id: list(range(store_id * 10, store_id * 10 + 10)) for store_id in store_ids}

# Date range
start_date = datetime(2025, 3, 10)
end_date = datetime(2025, 11, 5)

# File path (update this if needed)
file_location = r"C:\Users\mahakal.s\Documents\Retail_Project_Data"
os.makedirs(file_location, exist_ok=True)
csv_file_path = os.path.join(file_location, "sales_data.csv")

# Generate the CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["customer_id", "store_id", "product_name", "sales_date", "sales_person_id", "price", "quantity", "total_cost"])

    for _ in range(500000):
        customer_id = random.choice(customer_ids)
        store_id = random.choice(store_ids)
        product_name = random.choice(list(product_data.keys()))
        sales_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        sales_person_id = random.choice(sales_persons[store_id])
        quantity = random.randint(1, 10)
        price = product_data[product_name]
        total_cost = round(price * quantity, 2)

        csvwriter.writerow([
            customer_id,
            store_id,
            product_name,
            sales_date.strftime("%Y-%m-%d"),
            sales_person_id,
            price,
            quantity,
            total_cost
        ])

print("CSV file with sales data generated successfully!")
