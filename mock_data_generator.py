import json
import string
import csv
import random
import pandas
from datetime import date, timedelta

current_date = date.today()
transaction_per_day=10 
# Define customer and product IDs (replace with your actual data)
customer_ids = ["CUST00001", "CUST00002", "CUST00003", "CUST00004", "CUST00005"]
product_ids = ["PROD00001", "PROD00002", "PROD00003", "PROD00004", "PROD00005"]

# Define payment types
payment_types = ["Credit Card", "Debit Card", "Cash on Delivery"]

#Define Prices for each products
product_prices = {
    "PROD00001": 799.99,
    "PROD00002": 499.99,
    "PROD00003": 79.99,
    "PROD00004": 19.99,
    "PROD00005": 49.99,
    "PROD00006": 99.99,
    "PROD00007": 149.99,
    "PROD00008": 199.99,
    "PROD00009": 14.99,
    "PROD00010": 19.99,
}


def get_product_price(product_id):
    if product_id in product_prices:
        return product_prices[product_id]
    else:
        return 0.00
    

def generate_transaction(current_date):
    transaction_id= "TXN"+"".join(random.choices(string.digits, k=8))
    customer_id= random.choice(customer_ids)
    product_id= random.choice(product_ids)
    quantity= random.randint(1, 5)
    price= get_product_price(product_id)
    transaction_date= str(current_date)
    payment_type= random.choice(payment_types)
    status= "Completed"
    return {
        "transaction_id":  transaction_id,
        "customer_id":  customer_id,
        "product_id":  product_id,
        "quantity":  quantity,
        "price":  price,
        "transaction_date":  transaction_date,
        "payment_type":  payment_type,
        "status":  status
    }
    
def generate_transactions(no_of_transactions, current_date):
    transactions=[]
    for _ in range(no_of_transactions):
        transactions.append(generate_transaction(current_date))
    return transactions

def write_to_csv(data, filename):
    with open(filename, "w", newline="")as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["transaction_id", "customer_id", "product_id", "quantity",
                                                      "price", "transaction_date", "payment_type", "status"])
        writer.writeheader()
        writer.writerows(data)
        
def genearate_data(current_date):
    transactions = generate_transactions(transaction_per_day,current_date)
    write_to_csv(transactions,f"/tmp/transactions_{str(current_date)}.csv")
    print(f"Generated mock transaction data transactions_{str(current_date)}.csv and saved in csv files")
