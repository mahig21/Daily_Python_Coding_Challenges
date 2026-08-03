#25-08-26
"""
Given a string, return its camel case version using the following rules:

* Words in the string argument are separated by one or more characters from the 
  following set: space ( ), dash (-), or underscore (_). Treat any sequence of 
  these as a word break.
* The first word should be all lowercase.
* Each subsequent word should start with an uppercase letter, with the rest of it 
  lowercase.
* All spaces and separators should be removed.
"""
def to_camel_case(s):
    word_list=[]
    word=""
    camelCase=""
    for i in range(len(s)):
        if i==len(s)-1:
            word+=s[i]
            word_list.append(word)
        if s[i]==' ' or s[i]=="_" or s[i]=="-":
            if word!="":
                word_list.append(word)
                word=""
        else:
            word+=s[i]
    for i in range(len(word_list)):
        first=word_list[i][0]
        rest=word_list[i][1:]
        if i==0:
            camelCase+=first.lower()
            camelCase+=rest.lower()
        else:
            camelCase+=first.upper()
            camelCase+=rest.lower()
    return camelCase
s=input("Enter a string: ")
print(to_camel_case(s))