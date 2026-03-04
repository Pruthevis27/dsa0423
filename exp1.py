# Grocery Bill Calculation Program

n = int(input("Enter number of items: "))

prices = []
quantities = []

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    prices.append(price)
    quantities.append(quantity)

discount_rate = float(input("Enter discount rate (%): "))
tax_rate = float(input("Enter tax rate (%): "))

# Calculate subtotal
subtotal = 0
for i in range(n):
    subtotal += prices[i] * quantities[i]

# Calculate discount
discount = (discount_rate / 100) * subtotal
amount_after_discount = subtotal - discount

# Calculate tax
tax = (tax_rate / 100) * amount_after_discount

# Final total
total_cost = amount_after_discount + tax

print("\n----- BILL SUMMARY -----")
print("Subtotal:", subtotal)
print("Discount Amount:", discount)
print("Tax Amount:", tax)
print("Final Total Cost:", total_cost)