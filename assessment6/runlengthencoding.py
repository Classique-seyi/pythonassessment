word = input()

new_word = ""
count = 1

for i in range(len(word)):
    print(word[i])
    if i == len(word) - 1:
        new_word += word[i] + str(count)
        break
    # if word[i] == word[i+1:i+2]: # slicng was used because word[i+1] throws an exception (index out of range) when i = len(word) - 1
    if word[i] == word[i+1]:
        count += 1
    else:
        new_word += word[i] + str(count)
        count= 1
print(count)
print(new_word)