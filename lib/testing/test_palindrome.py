import pytest
from palindrome import longest_palindromic_substring

# Test case: string with multiple valid palindromes
def test_babad_returns_valid_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

# Test case: even-length palindrome
def test_cbbd_returns_bb():
    assert longest_palindromic_substring("cbbd") == "bb"

# Edge case: single character input
def test_single_character_returns_itself():
    assert longest_palindromic_substring("a") == "a"

# Edge case: two different characters (no palindrome longer than 1)
def test_two_different_characters_returns_one_character():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

# Test case: entire string is a palindrome
def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge case: empty string
def test_empty_string_returns_empty_string():
    assert longest_palindromic_substring("") == ""

# Edge case: all characters are the same
def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

# Edge case: no repeating characters
def test_no_long_palindrome_returns_single_character():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"

# Test case: palindrome exists within the string
def test_longer_palindrome_inside_word():
    assert longest_palindromic_substring("bananas") == "anana"

# Test case: long even-length palindrome
def test_even_length_long_palindrome():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

# Test case: palindrome with numbers
def test_palindrome_with_digits():
    assert longest_palindromic_substring("abc1234321xyz") == "1234321"

# Edge case: case sensitivity (uppercase vs lowercase)
def test_case_sensitivity():
    result = longest_palindromic_substring("Aa")
    assert result in ["A", "a"]