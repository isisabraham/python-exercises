n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))
a, b, c = n1, n2, n3
if a < b: a, b = b, a
if a < c: a, c = c, a
if b < c: b, c = c, b
print(a, b, c)  # descending
