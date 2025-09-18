p1 = float(input("Enter price of product 1: $ "))
p2 = float(input("Enter price of product 2: $ "))
p3 = float(input("Enter price of product 3: $ "))

cheapest = min(p1, p2, p3)

print(f"You should buy the product that costs: ${cheapest:.2f}")
