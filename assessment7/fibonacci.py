def fibonacci(number):
    if number <= 0:
        return []

    if number == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, number):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def even_sum(number):
    sequence = fibonacci(number)
    total = 0

    for num in sequence:
        if num%2 == 0:
            total += num
    return f"Sequence: {total}"

def reversed_fibonacci(number):
    sequence = fibonacci(number)

    rev_sequence = []
    for i in range(len(sequence) -1, -1, -1):
        rev_sequence.append(sequence[i])
    return rev_sequence


print(fibonacci(8))
print(even_sum(8))
print(reversed_fibonacci(8))


# n = int(input())
# a, b = 0, 1
# result = []
# for i in range(n):
#     result.append(str(a))
#     a, b = b, a + b
# print(" ".join(result))
