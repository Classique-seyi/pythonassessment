def decimal_to_binary(n):
    if n == 0:
        return "0"
    result = ""

    while n > 0:
        digit = n%2

        result += str(digit)

        n = n // 2
       
    return int(result[::-1])

print(decimal_to_binary(10))




