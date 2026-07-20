#25-04-26
"""
Given a compressed string, return the decompressed version using the following rules:

- The given string is made up of words and numbers separated by spaces.
- Leave the words unchanged.
- Replace numbers with the word at that position, where the first word is at position 1.
"""
def decompress(s):
    list_s=s.split()
    new_s=[]
    for i in list_s:
        if i.isdigit():
            new_s.append(list_s[int(i)-1])
        else:
            new_s.append(i)
    return " ".join(new_s)
s=input("Enter a compressed string: ")
new_s=decompress(s)
print(new_s)