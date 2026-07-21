#14-04-26
"""
Given a string, return the letter from the string that appears last in the alphabet.

- If two or more letters tie for the last in the alphabet, return the first one.
- Ignore all non-letter characters.
"""
alphabets="abcdefghijklmnopqrstuvwxyz"
def get_last_letter(s):
    maxIndex=0
    rev=s[::-1]
    for i in rev:
        if i.isalpha():
            if alphabets.index(i.lower())>=maxIndex:
                maxIndex=alphabets.index(i.lower())
                lastLetter=i
    return lastLetter
last_letter=get_last_letter("HeLl0")
print(last_letter)