"""
text_utils.py

Core text-processing logic for the Text Utility API.
Kept separate from Flask so these functions can be tested independently.
"""

def is_palindrome(text):
    """
    Check whether the given text is a palindrome.
    Ignores case, spaces, and punctuation.
    Example: "A man, a plan, a canal: Panama" -> True
    """
    # Keep only alphanumeric characters, and convert to lowercase.
    # This means "Racecar!" and "race car" both get reduced to "racecar".
    cleaned = ''.join(char.lower() for char in text if char.isalnum())

    # A palindrome reads the same forwards and backwards.
    # cleaned[::-1] is Python's slice syntax for "reverse this string."
    return cleaned == cleaned[::-1]

def word_count(text):
    """
    Count the number of words and characters in the given text.
    Returns a dictionary with both counts.
    Example: "Hello world" -> {"words": 2, "characters": 11}
    """
    # .split() with no arguments splits on whitespace and ignores
    # extra/leading/trailing spaces automatically.
    words = text.split()

    return {
        "words": len(words),
        "characters": len(text)
    }

def reverse_text(text):
    """
    Reverse the given text.
    Example: "Hello" -> "olleH"
    """
    return text[::-1]
