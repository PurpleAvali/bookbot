"""_summary_
Module:
    This is the main module and the entrypoint of the program
"""
from stats import count_words_in_string
from stats import count_chars_in_string
def get_book_text(filepath: str) -> str:
    """Reads the entire contents of a text file and returns it as a string.
    
    Args:
        filepath (str): The path to the text file to be read (e.g., "books/frankenstein.txt").
    
    Returns:
        str: The full contents of the file as a single string if successful.
             If the file is not found, returns an error message string.
    
    Raises:
        Prints a FileNotFoundError message to stdout if the file cannot be opened.
    """
    try:
        with open(filepath, "r", encoding="UTF-8") as f:
            contents = f.read()
        return contents
    except FileNotFoundError as e:
        print(e)
    return "Error: Either the file was not found, or you entered the wrong filepath?"


def main():
    """Main entry point of the script.
    
    Loads the text of "Frankenstein" from the predefined file path,
    counts the words in it, and prints the result to stdout.
    """
    text = get_book_text("books/frankenstein.txt")
    print(count_chars_in_string(text))

if __name__ == "__main__":
    main()