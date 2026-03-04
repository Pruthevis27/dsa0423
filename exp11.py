import numpy as np

# Fuel efficiency of different car models (in miles per gallon)
fuel_efficiency = np.array([18, 22, 25, 30, 28])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Compare two car models
model1 = fuel_efficiency[0]
model2 = fuel_efficiency[3]

# Calculate percentage improvement
percentage_improvement = ((model2 - model1) / model1) * 100

# Display results
print("Fuel Efficiency of Car Models:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
print("Model 1 Efficiency:", model1)
print("Model 2 Efficiency:", model2)
print("Percentage Improvement:", percentage_improvement, "%")