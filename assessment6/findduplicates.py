
numbers = input().split()

num_list = []

for number in numbers:
   
    num_list.append(int(number))

# seen = []
# duplicate = []

# for number in num_list:
#     if number in seen:
#         if number not in duplicate:
#             duplicate.append(number)
#     else:
#         seen.append(number)

# if not duplicate:
#     print([])
# else:
#     print(duplicate)

nums_count = {}
for num in num_list:
    if num not in nums_count:
        nums_count[num] = 1
    else:
        nums_count[num] += 1

dups = dict(filter(lambda val: val[1] > 1, nums_count.items()))
print(list(dups.keys()))


