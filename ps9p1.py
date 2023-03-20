def calculate_total(quantity, price):
    total = quantity * price
    if total > 100000:
        total *= 0.9
    return total
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
total = calculate_total(quantity, price)
print(f"Quantity: {quantity}")
print(f"Price: {price:.2f}")
print(f"Total: {total:.2f}")