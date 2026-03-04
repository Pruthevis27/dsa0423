import pandas as pd

# Create sample DataFrame
data = {
    'CustomerID': [101, 102, 101, 103, 102],
    'OrderDate': pd.to_datetime(['2025-01-01', '2025-01-05', 
                                  '2025-01-10', '2025-01-12', 
                                  '2025-01-15']),
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Tablet'],
    'Quantity': [1, 2, 1, 3, 2]
}

order_data = pd.DataFrame(data)

# 1. Total number of orders per customer
total_orders = order_data.groupby('CustomerID').size()

# 2. Average order quantity per product
avg_quantity = order_data.groupby('Product')['Quantity'].mean()

# 3. Earliest and Latest order dates
earliest_date = order_data['OrderDate'].min()
latest_date = order_data['OrderDate'].max()

print("Total Orders Per Customer:\n", total_orders)
print("\nAverage Quantity Per Product:\n", avg_quantity)
print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)