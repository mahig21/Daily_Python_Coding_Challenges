#03-09-26
"""
Given a word or sentence and a string of lowercase letters, determine if the word or
sentence uses all the letters from the given set at least once and no other letters.

- Ignore non-alphabetical characters in the word or sentence.
- Ignore letter casing in the word or sentence.
"""
def is_pangram(sentence, letters):
    sentence=sentence.lower()
    set_sent=set(sentence)
    set_sentence=set()    
    for i in set_sent:
        if i.isalpha():
           set_sentence.add(i)
    set_letters=set(letters)
    return set_letters==set_sentence

print(is_pangram("Hello World!", "helowrd"))