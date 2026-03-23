# Program to swap two integers without using third variable (arithmetic method)
a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))

print("Before swapping: a =", a, ", b =", b)

# Swap without temp: a = a + b; b = a - b; a = a - b
a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)
