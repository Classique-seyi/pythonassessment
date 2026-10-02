number1 = int(input("Enter your first number: "))

if isinstance(number1, int):
    first_number = number1
else:
    print("Wrong input")


number2 = int(input("Enter your second number: "))

if isinstance(number2, int):
   second_number = int(number2)
else:
    print("Wrong input")

operators = ["+", "-", "*", "/"]
operator = input("Enter your operator: ")

if operator not in operators:
    print("Output: Invalid operator")




if operator == "+":
    result = first_number + second_number
    print(f"Result: {result}")
elif operator == "-":
    result = first_number - second_number
    print(f"Result: {result}")
elif operator == "*":
    result = first_number * second_number
    print(f"Result: {result}")
elif second_number == 0:
    print("Output: Cannot divide by zero")
elif operator == "/":
    result = first_number / second_number
    print(f"Result: {result}")

