import math

# Program to find area and perimeter of triangle using Heron's formula
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Semi-perimeter
s = (a + b + c) / 2

# Area = sqrt[s(s-a)(s-b)(s-c)]
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Perimeter
perimeter = a + b + c

print("Area:", area)
print("Perimeter:", perimeter)
print(f"Triangle area: {area:.2f}, perimeter: {perimeter:.2f}")
