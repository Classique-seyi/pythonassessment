numbers = input("Enter a list of numbers: ").split()
targ = int(input("Enter a target number: "))

num_list = []
target = 0
target += targ

for number in numbers:
    num_list.append(int(number))


for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] + num_list[j] == target:
            print(f"Target: {target}  → {num_list[i]} + {num_list[j]}\nStretch requirement: {[i], [j]}")
else:
    print("No valid pair found")
