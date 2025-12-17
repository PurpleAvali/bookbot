def count_words_in_string(string: str) -> str:
    """Counts the number of words in the provided string.
    
    Words are separated by whitespace. Empty strings or multiple consecutive
    whitespace characters are handled gracefully (they do not add to the count).
    
    Args:
        string (str): The input text whose words will be counted.
    
    Returns:
        str: A formatted string indicating the total number of words found,
             e.g., "Found 12345 total words".
    """
    splits = string.split()
    num_words = 0
    for item in splits:
        if item != "":
            num_words += 1
    return f"Found {num_words} total words"
