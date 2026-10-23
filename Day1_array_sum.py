def sum_of_array_elements(arr):
    total = 0

    for num in arr:
        total += num

    return total

numbers = [1, 2, 3, 4, 5]
result = sum_of_array_elements(numbers)

print("Array:", numbers)
print("Sum of elements:", result)
