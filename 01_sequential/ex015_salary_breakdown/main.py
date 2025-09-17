hourly_wage = float(input("Enter your hourly wage (R$): "))
hours_worked = float(input("Enter hours worked this month: "))

gross = hourly_wage * hours_worked
ir = gross * 0.11      # Income Tax (IR)
inss = gross * 0.08    # INSS
union = gross * 0.05   # Union
net = gross - (ir + inss + union)

print(f"+ Gross Salary : R$ {gross:.2f}")
print(f"- IR (11%)     : R$ {ir:.2f}")
print(f"- INSS (8%)    : R$ {inss:.2f}")
print(f"- Union (5%)   : R$ {union:.2f}")
print(f"= Net Salary   : R$ {net:.2f}")
