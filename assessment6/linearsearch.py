numbers = input().split()

num_list = []

for number in numbers:
    num_list.append(int(number))

target = int(input())
count = 0
found = False
indices = [index for index, number in enumerate(num_list) if number == target]

for index, number in enumerate(num_list):
    
    if number == target:
        found = True
        count += 1

if not found:
    print("Target not found")
else:
    print(f'''Target: {target} - Found at indices: {indices} | Count: {count} | First: {indices[0]} | Last: {indices[-1]}''')


       


# for i in range(len(num_list)):

#     if num_list[i] == target:
#         count += 1
#         found = True

#     if not found:
#         print("Target not found")
           
    
