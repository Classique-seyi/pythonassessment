# Dynamic code that convert number to roman from 1 - 3999

def number_to_roman(number):
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Input must be integer")

    if number < 1 or number > 3999:
        raise ValueError("Integer must be between 1 and 3999")
    nums = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"   
    }
    roman = ""
  
    for key in nums:
        digit = number//key
        number = number%key
    
        word = digit * nums[key]
        roman += word
    return roman

print(number_to_roman(1))
print(number_to_roman(4))
print(number_to_roman(1994))
print(number_to_roman(2458))
print(number_to_roman(3999))
