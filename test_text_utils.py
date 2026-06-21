# test_text_utils.py
# Automated unit tests for text_utils.py.
# Run with: python -m unittest test_text_utils.py

import unittest
from text_utils import is_palindrome, word_count, reverse_text


class TestIsPalindrome(unittest.TestCase):
    """Tests for the is_palindrome function."""

    def test_simple_palindrome(self):
        # assertTrue checks that the value is truthy (True in this case).
        self.assertTrue(is_palindrome("racecar"))

    def test_not_a_palindrome(self):
        # assertFalse checks that the value is falsy (False in this case).
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_punctuation_and_spaces(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_empty_string_is_palindrome(self):
        # An empty string reversed is still an empty string, so this is technically true.
        self.assertTrue(is_palindrome(""))

class TestWordCount(unittest.TestCase):
    """Tests for the word_count function."""

    def test_normal_sentence(self):
        # assertEqual checks that two values are exactly equal.
        self.assertEqual(word_count("Hello world"), {"words": 2, "characters": 11})

    def test_empty_string(self):
        self.assertEqual(word_count(""), {"words": 0, "characters": 0})

    def test_extra_whitespace_does_not_inflate_word_count(self):
        # Multiple spaces between words shouldn't be counted as extra words.
        self.assertEqual(word_count("Hello    world"), {"words": 2, "characters": 14})


class TestReverseText(unittest.TestCase):
    """Tests for the reverse_text function."""

    def test_normal_string(self):
        self.assertEqual(reverse_text("Hello world"), "dlrow olleH")

    def test_empty_string(self):
        self.assertEqual(reverse_text(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_text("a"), "a")

if __name__ == '__main__':
    unittest.main()