g1 = float(input("Grade 1: "))
g2 = float(input("Grade 2: "))
avg = (g1 + g2) / 2
if avg == 10:
    print("Approved with Distinction")
elif avg >= 7:
    print("Approved")
else:
    print("Failed")
