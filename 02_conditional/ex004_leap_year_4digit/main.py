year = input("Enter a 4-digit year: ").strip()
if len(year) == 4 and year.isdigit():
    y = int(year)
    is_leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    print("Leap year" if is_leap else "Not leap year")
else:
    print("Invalid year format")
