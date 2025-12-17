def get_book_text(filepath: str) -> str:
   
    try: 
        with open(filepath, "r") as f:
            contents = f.read()
        return contents
    except FileNotFoundError as e:
        print(e)
    return("Error: Either the file was not found, or you entered the wrong filepath?")

def count_words_in_string(string: str) -> str:
    splits = string.split()
    num_words = 0
    for item in splits:
        if item != "":
            num_words += 1
    return f"Found {num_words} total words"
            
def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words_in_string(text))

if __name__ == "__main__":
    main()