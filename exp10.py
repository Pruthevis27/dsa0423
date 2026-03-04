import matplotlib.pyplot as plt

# Data for months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Temperature data (°C)
temperature = [25, 28, 32, 35, 38, 36]

# Rainfall data (mm)
rainfall = [10, 20, 35, 50, 80, 60]

# Line plot for temperature
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()

# Scatter plot for rainfall
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()