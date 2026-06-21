numbers = [4, 6, 2, 3, 1, 7, 5]

n = len(numbers)
reversed_numbers = []

for i in range(n-1, -1, -1):
    reversed_numbers.append(numbers[i])

print(reversed_numbers)