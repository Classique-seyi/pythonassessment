num = int(input("Enter your number: "))

result = 0

while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10
print(result)



# n = int(input())

# # Multiply the digits and print the product
# result = 1
# while n > 0:
#   digit = n % 10
#   result *= digit
#   n = n // 10
# print(result)