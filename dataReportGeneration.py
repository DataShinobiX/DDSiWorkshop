# Assignment 1.1
#This code is to generate profiling report on CSV data. 


import pandas as pd
from ydata_profiling import ProfileReport

transactions = pd.read_csv('Comfy_Data/Transactions.csv', sep = ';') 
customers = pd.read_csv('Comfy_Data/Client_information.csv', sep = ';')

# Display basic information about the datasets
print("Transactions Dataset Information:")
transactions.info()
print("\n\nCustomers Dataset Information:")
customers.info()

# Show summary statistics
print("\nTransactions Dataset Summary Statistics:")
transactions.describe()
print("\n\nCustomers Dataset Summary Statistics:")
customers.describe()

# Generate pandas-profiling report for transactions dataset
profile_transactions = ProfileReport(transactions, title="Transactions Data Quality Report")
profile_transactions.to_file("Reports/transactions_data_quality_report.html")

# Generate pandas-profiling report for customers dataset
profile_customers = ProfileReport(customers, title="Customers Data Quality Report")
profile_customers.to_file("Reports/customers_data_quality_report.html")