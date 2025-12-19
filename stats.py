
def count_words_in_string(content: str) -> int:
    return len(content.split())
   
def count_chars_in_string(content :str) -> dict[str, int]:
    count = {"": 0}
    for c in content.lower():
        count[c] = count.get(c, 0) + 1
    return count

def ordered_list_of_dicts(freq: dict) -> list:
    if '' in freq:
        freq[' '] = freq.pop('')

    list_dicts = [{"char": char, "num": count} for char, count in freq.items()]
    list_dicts = sorted(list_dicts, key=lambda x: x["num"], reverse=True)
    
    return list_dicts

def print_pretty_dict(list: list[dict]):
    for i in list:
        if i["char"] != "\n":
            print(f"{i["char"]}: {i["num"]}")