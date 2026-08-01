#16-08-26
#Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
#Ignore casing and white space.

def are_anagrams(str1, str2):
    set1=set(str1.lower())
    set2=set(str2.lower())
    str1=list(set1)
    str2=list(set2)
    str1.sort()
    str2.sort()
    return str1==str2
str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
print(are_anagrams(str1, str2))