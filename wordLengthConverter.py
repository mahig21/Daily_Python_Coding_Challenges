#11-03-26
"""
Given a string of words, return a new string where each word is replaced by its length.

* Words in the given string will be separated by a single space
* Keep the spaces in the returned string.
"""
def convert_words(s):
    words=s.split()
    lengths=[]
    for i in words:
        lengths.append(str(len(i)))
    return " ".join(lengths)
lengths=convert_words("The quick brown fox jumps over the lazy dog")
print(lengths)