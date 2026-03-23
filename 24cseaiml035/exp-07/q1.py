m = int(input("enter m: "))
n = int(input("enter n: "))
natural_numbers = []
for num in range(m, n + 1):
    natural_numbers.append(num)
print("List of natural numbers from", m, "to", n, ":", natural_numbers)

# Calculate sum
total_sum = sum(natural_numbers)
print("Sum of the numbers:", total_sum)

# Calculate average
if natural_numbers:
    average = total_sum / len(natural_numbers)
    print("Average of the numbers:", average)
else:
    print("Average: N/A (empty list)")

# Find largest
if natural_numbers:
    largest = max(natural_numbers)
    print("Largest number:", largest)
else:
    print("Largest: N/A (empty list)")

# Find smallest
if natural_numbers:
    smallest = min(natural_numbers)
    print("Smallest number:", smallest)
else:
    print("Smallest: N/A (empty list)")

# Create new list excluding numbers divisible by 3
filtered_list = [num for num in natural_numbers if num % 3 != 0]
print("List excluding numbers divisible by 3:", filtered_list)
