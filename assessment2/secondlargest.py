numbers = input("Enter a list of numbers: ").split()

list_num = []
for number in numbers: 
    list_num.append(int(number))
# print(list_num)

unique = set(list_num)
# print(unique)
largest = 0
for number in list_num:
    if number > largest:
        largest = number
unique.remove(largest)        
second_largest = max(unique)
print(f"Output: {second_largest}")



# for number in numbers:
#     largest = max(numbers)
#     if number < largest or number > largest:

#         second_largest = number
#     print({second_largest})