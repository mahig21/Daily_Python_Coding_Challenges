#24-04-26
"""
Given a string, return a compressed version of the string using the following rules:

* The first occurrence of a word remains unchanged.
* Subsequent occurrences are replaced with the position of the first
  occurrence, where the first word is at position 1.
* Words are separated by a single space.
"""
def compress(s):
    new_s=[]
    list_s=s.split()
    for i in list_s:
        if i not in new_s:
            new_s.append(i)
        else:
            new_s.append(str(list_s.index(i)+1))
    return " ".join(new_s)
s=input("Enter a string to compress: ")
new_s=compress(s)
print(new_s)