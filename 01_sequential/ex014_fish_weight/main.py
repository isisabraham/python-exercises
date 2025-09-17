weight = float(input('Enter the fish weight in kg: '))

limit = 50
fine_per_kg = 4.0

if weight > limit:
    excess = weight - limit
    fine = excess * fine_per_kg
else:
    excess = 0
    fine = 0

print(f'Excess: {excess} kg')
print(f'Fine: R$ {fine:.2f}')
