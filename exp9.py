import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [20000, 25000, 18000, 30000, 28000, 35000]

# Line Plot
plt.plot(months, sales)
plt.title("Monthly Sales Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Bar Plot
plt.bar(months, sales)
plt.title("Monthly Sales Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()