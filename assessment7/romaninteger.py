def roman_to_integer(word):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    i = 0
    while i < len(word)-1:

        if roman[word[i]] < roman[word[i+1]]:
            total -= roman[word[i]]
        else:
            total += roman[word[i]]

        i += 1
    total += roman[word[-1]]
 
    return total

# def roman_to_integer(word):
#     roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#     total = 0
#     i = 0
#     while True:
#         for i in range(len(word)- 1):
#             if roman[word[i]] < roman[word[i+1]]:
#                 total -= roman[word[i]]
#             else:
#                 total += roman[word[i]]
#             i += 1
#         total += roman[word[-1]]
#         return total


print(roman_to_integer("III"))
print(roman_to_integer("VI"))
print(roman_to_integer("IV"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))