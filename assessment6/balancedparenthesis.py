word = input()

# count = 0

# for char in word:
#     if char == "(":
#         count += 1
#     elif char == ")":
#         count -= 1
#     elif char == "[":
#         count += 1
#     elif char == "]":
#         count -= 1
#     elif char == "{":
#         count += 1
#     elif char == "}":
#         count -= 1

#     if count < 0:
#         break
# if count == 0:
#     print("Balanced")
# else:
#     print("Not balanced")

stack = []
openings = ['(', '[', '{']
closings = {'}': '{', ']': '[', ')': '('}
all_parentheses = 0

for ch in word:
    if ch in openings:
        stack.append(ch)
        all_parentheses += 1
    if ch in closings and stack and closings[ch] == stack[-1]:
        stack.pop()
    if ch in closings:
        all_parentheses += 1


if stack or all_parentheses % 2 != 0:
    print('Not balanced')
else:
    print('Balanced')



