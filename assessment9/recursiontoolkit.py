def digit_sum(n):
    if n == 0:
        return 0
    
    digit = n%10
    num = n // 10
    
    return digit + digit_sum(num)

print(digit_sum(1234))
print(digit_sum(0))


def reverse_text(text):
    if not text:
        return ""

    last = text[-1]
    new_text = text[:-1]

    return last + reverse_text(new_text)

print(reverse_text("python"))
print(reverse_text(""))


def count_char(text, ch):
    count = 0

    if text == "":
        return 0

    if text[0] == ch:
        count += 1

    return count + count_char(text[1:], ch)


print(count_char("banana", "a"))

def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    return base * power(base, exp-1)


print(power(2, 10))
print(power(5, 0))