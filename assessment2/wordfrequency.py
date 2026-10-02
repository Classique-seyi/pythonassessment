sentence = input("Enter your sentence: ")

# sentence = "python is fun and python is powerful"

words = sentence.lower().split()
text = {}

for word in words:
    if word in text:
        text[word] += 1
    else:
        text[word] = 1
print(text)

