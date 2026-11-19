numbers = input().split()

num_list = []

for num in numbers:
    num_list.append(int(num))

smallest = num_list[0]
largest = num_list[0]
total = 0
for number in num_list:
    if number < smallest:
        smallest = number
    elif number > largest:
        largest = number
    total += number
    average = total / len(num_list)


print(f'''Smallest: {smallest}
Largest: {largest}
Total: {total}
Average: {average}
'''
)