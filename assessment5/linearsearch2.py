numbers = input().split()

num_list = []

for number in numbers:
    num_list.append(int(number))
print(num_list)

target = int(input())

found = False

for index, number in enumerate(num_list):
    if number == target:
        print(f"Found at index {index}")
        found = True

    if not found:
        print("Target not found")