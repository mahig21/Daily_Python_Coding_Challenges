#06-07-2026
# Given a string, return only the words that are entirely lowercase, 
# in their original order and with a space between each word.
def get_lowercase_words(s):
    L=s.split()
    str1=[]
    for i in L:
        if i.islower():
            str1+=[i]
    return ' '.join(str1)
string=input()
s=get_lowercase_words(string)
print(s)