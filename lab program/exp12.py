import pandas as pd

# Sample sales dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Keyboard', 'Mouse', 'Camera'],
    'Quantity': [50, 120, 80, 60, 40, 90, 30]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Sort products by quantity sold (descending)
top_products = sales_data.sort_values(by='Quantity', ascending=False)

# Get top 5 products
top5 = top_products.head(5)

print("Top 5 Most Sold Products:")
print(top5)