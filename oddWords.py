#21-04-26
"""
Given a string of words, return only the words with an odd number of letters.

* Words in the given string will be separated by a single space.
* Return the words separated by a single space.
"""
def get_odd_words(s):
    words=s.split()
    odd_str=[]
    for i in words:
        if len(i)%2!=0:
            odd_str.append(i)
    return " ".join(odd_str)
odd_str=get_odd_words("banana split sundae with rainbow sprinkles on top")
print(odd_str)