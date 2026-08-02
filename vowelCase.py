#06-01-26
"""
    Given a string, return a new string where all vowels are converted to uppercase and
    all other alphabetical characters are converted to lowercase.

    - Vowels are "a", "e", "i", "o", and "u" in any case.
    - Non-alphabetical characters should remain unchanged.
    """
vowel="aeiou"
def vowel_case(s):
    vowelcase=""
    for i in s:
        if i.lower() in vowel:
            vowelcase+=i.upper()
        else:
            vowelcase+=i.lower()
    return vowelcase
print(vowel_case("HELLO, world!"))