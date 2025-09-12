def find_longest_word(document, longest_word=""):
    new_longest= ""
    if document.strip() == "":
        return ""
    
    words = document.split(maxsplit=1)
    if len(words) <1:
        return longest_word
    if len(words[0])> len(longest_word):
        longest_word= words[0]
    if len(words)<2:
        return longest_word
    return find_longest_word(words[1],longest_word)


print(find_longest_word("I am happy",""))
