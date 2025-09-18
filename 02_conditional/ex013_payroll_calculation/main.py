hour_rate = float(input("Enter hourly rate: $ "))
hours = float(input("Enter hours worked in the month: "))

# Gross salary
gross = hour_rate * hours

# Income Tax (IR)
if gross <= 900:
    ir_percent = 0
elif gross <= 1500:
    ir_percent = 0.05
elif gross <= 2500:
    ir_percent = 0.10
else:
    ir_percent = 0.20

ir = gross * ir_percent
union = gross * 0.03
fgts = gross * 0.11   # Not deducted
total_deductions = ir + union
net = gross - total_deductions

print(f"Gross salary:          ${gross:.2f}")
print(f"(-) IR ({ir_percent*100:.0f}%):        ${ir:.2f}")
print(f"(-) Union (3%):        ${union:.2f}")
print(f"FGTS (11%):            ${fgts:.2f}")
print(f"Total deductions:      ${total_deductions:.2f}")
print(f"Net salary:            ${net:.2f}")
