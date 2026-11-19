numbers = [14, 7, 22, 9, 7, 31]
target = int(input())

found = False

for i, num in enumerate(numbers):
    if num == target:
        print(f"Found at index {i}") 
        found = True
        break
        
    if not found:
        print("Target not found")



# for number in num_list:
#     number_index = [i for i, number in enumerate(num_list) if number == target]
#         print(f"Found at index {number_index}")
#         break 
#     print("Target not found")



# for number in num_list:
#     number_index = num_list.index(number)
# if number == target:
#     print(f"Found at index {number_index}")
# else:
#     print("Target not found")