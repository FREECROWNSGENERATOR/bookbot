def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    char_counts = {}

    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_chars_by_count(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_dict = ({"char": char, "count": count})
        chars_list.append(chars_dict)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
