#20-01-26
"""
    Given a string representing a variable name, convert it to consonant case using the 
    following rules:

    - All consonants should be converted to uppercase.
    - All vowels (a, e, i, o, u in any case) should be converted to lowercase.
    - All hyphens (-) should be converted to underscores (_).
    """
vowel="aeiou"
def to_consonant_case(s):
    vowelcase=""
    for i in s:
        if i.isalpha():
            if i.lower() in vowel:
                vowelcase+=i.lower()
            else:
                vowelcase+=i.upper()
        else:
            if i=="-":
                vowelcase+="_"
            else:
                vowelcase+=i
    return vowelcase
s=input("Enter a string: ")
print(to_consonant_case(s))