numbers = [5, 3, 8, 13, 17, 12, 88, 95, 94, 93, 74]

# Algorithm
largest = numbers[0]
for i in numbers[1:]:
    if i > largest:
        largest = i

print(f"Largest number: {largest}")