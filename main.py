with open("books/frankenstein.txt") as f:
    file_contents = f.read()

chars = {}
for c in file_contents.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1


def sort_dict_by_values(input_dict):
    sorted_items= sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

sorted_chars = sort_dict_by_values(chars)

for key, value in sorted_chars.items():
    if key.isalpha():
        print(f"The '{key}' character was found {value} times")