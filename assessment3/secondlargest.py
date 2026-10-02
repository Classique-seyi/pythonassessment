num = input("Enter a list of number: ").split()

num_list = []

for number in num:
    num_list.append(int(number))

unique = set(num_list)

largest = 0
for number in unique:
    if number > largest:
        largest = number
unique.remove(largest)
second_largest = max(unique)
print(f"Output: {second_largest}")