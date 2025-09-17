import math

area = float(input("Enter area to paint (m²): "))
coverage_per_liter = 6.0

# add 10% slack
liters_needed = (area / coverage_per_liter) * 1.10

can_liters, can_price = 18.0, 80.0
gal_liters, gal_price = 3.6, 25.0

# Option 1: only cans
only_cans = math.ceil(liters_needed / can_liters)
only_cans_cost = only_cans * can_price

# Option 2: only gallons
only_gals = math.ceil(liters_needed / gal_liters)
only_gals_cost = only_gals * gal_price

# Option 3: mixed (search the cheapest valid combo)
best_cost = float("inf")
best_cans = best_gals = 0
max_cans = math.ceil(liters_needed / can_liters)
for cans in range(0, max_cans + 1):
    remaining = max(liters_needed - cans * can_liters, 0)
    gals = math.ceil(remaining / gal_liters) if remaining > 0 else 0
    cost = cans * can_price + gals * gal_price
    if cost < best_cost:
        best_cost, best_cans, best_gals = cost, cans, gals

print(f"Liters needed with 10% slack: {liters_needed:.2f} L\n")

print("Buying only 18 L cans:")
print(f"  Cans: {only_cans}  | Cost: R$ {only_cans_cost:.2f}")

print("Buying only 3.6 L gallons:")
print(f"  Gallons: {only_gals}  | Cost: R$ {only_gals_cost:.2f}")

print("Mixed (cheapest):")
print(f"  Cans: {best_cans}, Gallons: {best_gals}  | Cost: R$ {best_cost:.2f}")
