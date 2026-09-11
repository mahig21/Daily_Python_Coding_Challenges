#11-09-26
"""
Given a string of words, return a new string with the words in reverse order. For
example, the first word should be at the end of the returned string, and the last word
should be at the beginning of the returned string.

- In the given string, words can be separated by one or more spaces.sed or
"""
def reverse_sentence(sentence):
    words=sentence.split()
    reverse=words[::-1]
    return " ".join(reverse)

print(reverse_sentence("npm  install   apt    sudo"))