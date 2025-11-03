def get_num_words(text):
    words = text.split()
    return len(words)  

def get_char_counts(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(char_counts):
    items = []
    for ch, count in char_counts.items():
        if ch.isalpha():  # skip spaces, punctuation, digits, etc.
            items.append({"char": ch, "num": count})
    items.sort(reverse=True, key=sort_on)
    return items
