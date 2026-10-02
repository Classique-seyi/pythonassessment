word = input(f"What is your word: ").lower()

if len(word) <= 1:
    print("Not a palindrome")
else:
    left = 0
    right = len(word) - 1
    if word[left] != word[right]:
        print("Not a palindrome")
        left += 1
        right -= 1
    else:
        print(f"{word} is a palindrome")
