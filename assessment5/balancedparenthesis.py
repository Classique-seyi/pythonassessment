sentence = input("Enter your sentence:")

par = 0
for char in sentence:
    if char == "(":
        par += 1
    elif char == ")":
        par -= 1

    if par < 0:
        break

if par == 0:
    print("Output: Balanced")
else:
    print("OUtput: Not Balanced")