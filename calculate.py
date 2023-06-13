def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
number_list = [1, 2, 3, 4, 5]
result = calculate_sum(number_list)
print(f"The sum of the numbers is: {result}")
