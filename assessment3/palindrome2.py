def palindrome(sentence):
    left = 0
    right = len(sentence) - 1

    while left < right:
        if not sentence[left].isalnum():
            left += 1
            continue
        if not sentence[right].isalnum():
            right -= 1
            continue
        if sentence[left] != sentence[right]:
            return False
        left += 1
        right -= 1
        return True

sentence = input("Enter your sentence: ").lower().strip()
if palindrome(sentence):
    print("Output: Palindrome")
else:
    print("Output: Not a Palindrome")


# palindrome("was it a car or a cat I saw?")