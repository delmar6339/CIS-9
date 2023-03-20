def calculate_mpg(miles, gallons):
    mpg = miles / gallons
    return mpg
def calculate_cost(gallons):
    cost = gallons * 2.5
    return cost
destination_city = input("Enter destination city: ")
miles_travelled = float(input("Enter miles travelled: "))
gallons_used = float(input("Enter gallons used: "))
mpg = calculate_mpg(miles_travelled, gallons_used)
cost = calculate_cost(gallons_used)
print(f"Destination city: {destination_city}")
print(f"Miles travelled: {miles_travelled}")
print(f"Gas cost: ${cost:.2f}")