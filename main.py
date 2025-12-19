"""_summary_
Module:
    This is the main module and the entrypoint of the program
"""
from stats import count_words_in_string
from stats import count_chars_in_string
from stats import ordered_list_of_dicts
from stats import print_pretty_dict
import sys

def get_book_text(filepath: str) -> str:
    
    try:
        with open(filepath, "r", encoding="UTF-8") as f:
            contents = f.read()
        return contents
    except FileNotFoundError as e:
        print(e)
        return "Error: Either the file was not found, or you entered the wrong filepath?"



def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        book_contents = get_book_text(filepath=filepath)
        num_words = count_words_in_string(book_contents)
        num_chars = count_chars_in_string(book_contents)
        char_list = ordered_list_of_dicts(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        print_pretty_dict(char_list)
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

if __name__ == "__main__":
    main()