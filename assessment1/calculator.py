
first_number = float(input(f"First number:"))
operator = input(f"Operator: ").strip()
second_number = float(input(f"Second number: "))



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
    print("Result: Cannot divide by zero")
elif operator == "/":
    result = first_number / second_number
    print(f"Result: {result}")
else:
    print("Result: Invalid operator")