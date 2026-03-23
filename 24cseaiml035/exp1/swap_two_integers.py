# Program to swap two integers using third variable
a = int(input("Enter first integer (a): "))
b = int(input("Enter second integer (b): "))

print("Before swapping: a =", a, ", b =", b)

# Swap using temp
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
