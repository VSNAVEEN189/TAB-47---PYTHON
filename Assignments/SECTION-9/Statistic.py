'''Manual Statistics
Looping over a list to compute stats by hand
Read 5 numbers into a list. WITHOUT using the built-in sum(), min(), or max(), compute and print:
• the list sorted in ascending order
• the list reversed
• the sum
• the average
• the maximum and the minimum'''

 # Read 5 numbers into a list
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

# 1. Sort the list in ascending order
sorted_list = list(numbers)
n = len(sorted_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

# 2. Reversed the list manually
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# 3. Compute Sum, Max, and Min using a single loop
total_sum = 0
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    total_sum += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# 4. Compute Average
average = total_sum / len(numbers)

# Print the results
print("\n--- Results ---")
print("Original list:", numbers)
print("Sorted (Ascending):", sorted_list)
print("Reversed list:", reversed_list)
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
