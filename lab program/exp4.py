import pandas as pd

# Create sample property data
data = {
    'PropertyID': [1, 2, 3, 4],
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi'],
    'Bedrooms': [3, 5, 4, 6],
    'Area_sqft': [1200, 2000, 1500, 2500],
    'ListingPrice': [5000000, 8000000, 6000000, 10000000]
}

property_data = pd.DataFrame(data)

# 1. Average listing price per location
avg_price = property_data.groupby('Location')['ListingPrice'].mean()

# 2. Properties with more than 4 bedrooms
more_bedrooms = property_data[property_data['Bedrooms'] > 4]
count_bedrooms = len(more_bedrooms)

# 3. Property with largest area
largest_area_property = property_data.loc[property_data['Area_sqft'].idxmax()]

print("Average Listing Price per Location:\n", avg_price)
print("\nNumber of Properties with more than 4 bedrooms:", count_bedrooms)
print("\nProperty with Largest Area:\n", largest_area_property)