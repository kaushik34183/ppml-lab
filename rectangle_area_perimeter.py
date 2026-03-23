# Program to find area and perimeter of rectangle
# Input dimensions
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calculate
area = length * width
perimeter = 2 * (length + width)

# Print results
print("Area:", area)
print("Perimeter:", perimeter)
print(f"Rectangle area: {area}, perimeter: {perimeter}")
