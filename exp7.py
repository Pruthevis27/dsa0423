import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1200, 5000000],
    [5, 2000, 8500000],
    [4, 1500, 6000000],
    [6, 2500, 10000000],
    [2, 900, 3500000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Extract sale prices (3rd column)
sale_prices = filtered_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

print("Average Sale Price (Bedrooms > 4):", average_price)