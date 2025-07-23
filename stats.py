def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_chars_dict(dict):
    sorted = []
    for (char, count) in dict.items():
        if char.isalpha():
            sorted.append({"char": char, "count": count })
    sorted.sort(reverse=True, key=lambda item: item["count"])
    return sorted