import pandas as pd

# Create sample sales data
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Price': [50000, 20000, 30000],
    'Quantity': [2, 3, 1]
}

sales_data = pd.DataFrame(data)

# Calculate Total Sales
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Display result
print(sales_data)