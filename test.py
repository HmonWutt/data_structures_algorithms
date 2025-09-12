
from pydoc import doc


def find_longest_word(document, longest_word=""):
    current_longest = longest_word
    new_longest= ""
    if len(document.split(maxsplit=1)) <2:
        if len(document)-1 > len(longest_word):
            return document[:-1]
        return longest_word
        
    words = document.split(maxsplit=1)
    if len(words[0])> len(current_longest):
        new_longest = find_longest_word(words[1],words[0])
    else:
        new_longest = find_longest_word(words[1],current_longest)
    if len(current_longest)<len(new_longest):
        current_longest = new_longest
    return current_longest

print(find_longest_word("Either that wallpaper goes, or I do.", ""))

