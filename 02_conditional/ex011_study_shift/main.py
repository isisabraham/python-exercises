shift = input("Enter your study shift (M = Morning, V = Afternoon, N = Night): ").upper()

if shift == "M":
    print("Good morning!")
elif shift == "V":
    print("Good afternoon!")
elif shift == "N":
    print("Good evening!")
else:
    print("Invalid value!")
