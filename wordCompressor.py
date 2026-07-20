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
new_s=compress("lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero")
print(new_s)