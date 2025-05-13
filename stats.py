def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lower = text.lower()
    count_dict = {}
    for char in text_lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def report_count(count_dict):
    char_list = []

    for char, count in count_dict.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

  
