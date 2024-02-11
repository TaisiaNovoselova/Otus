def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
