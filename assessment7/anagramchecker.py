def anagram_checker(word1, word2):
    if not word1 or not word2:
        return None
    word_dict = {}
    word_dict2 = {}
    for char in word1.lower():
        if char in word_dict:
            word_dict[char] += 1
            
        else:
            word_dict[char] = 1
    
    for char in word2.lower():
        if char in word_dict2:
            word_dict2[char] += 1
        else:
            word_dict2[char] = 1
    

    try:
        if word_dict != word_dict2:
            return "Not an Anagram"
        else:
            return "Anagram"
    except KeyError:
        return "Not correct"


print(anagram_checker("okay", "yoka"))
print(anagram_checker("kh", "ihn"))
print(anagram_checker("Dormitory", "dirtyroom"))
print(anagram_checker("hello", "world"))