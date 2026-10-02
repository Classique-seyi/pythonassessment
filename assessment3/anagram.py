word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")


for char in word1, word2:
    if char and len(word1) == len(word2):
        print("Anagram")
        break
    else:
        print("Not an Anagram")
        break



# if len(word1) == len(word2):
#     try:
#         for char in word1, word2:
#             # for ch in word2:
#             if char:
#                 print("Anagram")
#             else:
#                 print("Not an Anagram")
#             # break

#     except IndexError:
#         print("Not an Anagram")
#     # else:
#     #     print("Not an Anagram")