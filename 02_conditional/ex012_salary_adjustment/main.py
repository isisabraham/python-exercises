salary = float(input("Enter salary: $ "))

if salary <= 280:
    percent = 0.20
elif salary <= 700:
    percent = 0.15
elif salary <= 1500:
    percent = 0.10
else:
    percent = 0.05

increase = salary * percent
new_salary = salary + increase

print(f"Previous salary: ${salary:.2f}")
print(f"Applied percentage: {percent * 100:.0f}%")
print(f"Increase amount: ${increase:.2f}")
print(f"New salary: ${new_salary:.2f}")
