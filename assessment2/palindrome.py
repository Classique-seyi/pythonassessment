word = input("Enter your word: ").lower()

if len(word) <= 1:
    print("Output: Not a palindrome")
else:
    right = word[0]
    left = word[len(word) - 1]

    for letter in word:
        if right == left:
            print("Output: Palindrome")
            break
        else:
            print("Output: Not a palindrome")
            break