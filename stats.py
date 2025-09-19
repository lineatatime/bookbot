def sort_on(items):
    return items["num"]

def number_of_words(text):
    words = text.split()
    return f"Found {len(words)} total words"

def character_count(text):
    char_count = {}
    text = text.lower()
    for t in text:
        if t in char_count:
            char_count[t] = char_count[t] + 1
        else: char_count[t] = 1
    return char_count

def dictionary_sort(char_count):
    char_list = []
    for i in char_count:
        char_dict = {}
        char_dict["char"] = i
        char_dict["num"] = char_count[i]
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list