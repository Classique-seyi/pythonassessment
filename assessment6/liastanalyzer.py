numbers = input().split()

num_list = []

for number in numbers:
    num_list.append(int(number))


smallest = num_list[0]
largest = num_list[0]
total = 0
average = 0
count = 0


for i in range(len(num_list)):

    total += num_list[i]
    average = total / len(num_list)

    if num_list[i] <  smallest:
        smallest = num_list[i]
        smallest_index = i

    if num_list[i] > largest:
        largest = num_list[i]
        largest_index = i

    # elif num_list[i] > average:
    #     count += 1

for num in num_list :
    if num > average :
        count += 1

print(f'''Smallest: {smallest} (at index {smallest_index})
Largest: {largest} (at index {largest_index})
Total: {total}
Average: {average:.2f}
Numbers above average: {count}
''')