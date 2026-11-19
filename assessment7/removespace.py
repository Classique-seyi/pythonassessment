def remove_spaces(sentence):
    
    new_word = ""
    for i in range(len(sentence)):
        char = sentence[i]
        if i == 0 or sentence[i-1] == " ":
            if "a" <= sentence[i] <= "z":
                char = chr(ord(sentence[i]) - 32)
        if sentence[i] != " ":
            new_word += char
    return new_word



text = "i love python"
print(remove_spaces(text))