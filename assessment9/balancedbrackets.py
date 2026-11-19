def is_balanced(text):

    stack = []
    openings = ["(", "[", "{"]
    closings = {
        ")": "(",
        "]": "[",
        "}": "{"
        }

    for char in text:
        if char in openings:
            stack.append(char)
        if char in closings:
            if not stack:
                return False
            last = stack.pop()
            if last != closings[char]:
                return False

    if not stack:
        return True
    return False



print(is_balanced("(a + b) * [c - d]"))   # True
print(is_balanced("{[()]}"))              # True
print(is_balanced("([)]"))               # False
print(is_balanced("(("))                  # False
print(is_balanced("}{"))                 # False
print(is_balanced(""))                # True