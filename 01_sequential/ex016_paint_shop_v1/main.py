import math

area = float(input("Enter area to paint (m²): "))
coverage_per_liter = 3.0
liters_needed = area / coverage_per_liter

can_liters = 18.0
can_price = 80.0

cans = math.ceil(liters_needed / can_liters)
total_price = cans * can_price

print(f"Liters needed (no slack): {liters_needed:.2f} L")
print(f"Cans of 18 L: {cans}")
print(f"Total price: R$ {total_price:.2f}")
