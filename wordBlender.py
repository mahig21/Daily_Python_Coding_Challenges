#21=07-26
"""
Word Blender

Given two words, return a new word by combining the first half of the first
word with the second half of the second word.

- For odd-length words, the first half is the shorter half.
"""
def blend_words(word1, word2):
    len1=len(word1)
    len2=len(word2)
    index1=len1//2
    index2=len2//2
    fh_word1=word1[:index1]
    sh_word2=word2[index2:]
    return fh_word1+sh_word2
new_word=blend_words("hyena", "iguana")
print(new_word)