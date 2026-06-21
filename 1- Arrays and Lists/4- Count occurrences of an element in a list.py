items = ["apple", "banana", "apple", "orange", "banana", "apple"]
target = "banana"

counter = 0
for i in items:
    if i == target:
        counter = counter + 1

print(f"{target} appears {counter} times")