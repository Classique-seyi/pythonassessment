sentence = input("Enter a sentence: ").lower().strip().replace(" ", "")

punctuations = [",", ".", "-", "_", "!", ":", ";", "?"]



fixed = ""
for x in punctuations:
    if x in sentence:
        print("There's a punctuation let's remove it")
        print("Fixing...")
        sentence = sentence.replace(x, "")
    
left = 0
right = len(sentence) - 1


while left < right:

    
    if sentence[left]== sentence[right]:
        left +=1
        right -=1

        print("Output: Palindrome")
        break

    else:
        print("Output: Not a Palindrome")
        break
