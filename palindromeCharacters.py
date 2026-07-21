#07-04-26
"""
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

* A palindrome is a string that is the same forward and backward.
* If it's not a palindrome, return "none".
"""
def palindrome_locator(s):
    rev=s[::-1]
    len1=len(s)
    if s==rev:
        if len1%2!=0:
            return s[len1//2]
        else:
            return s[(len1//2)-1]+s[len1//2]
    return "none"
s=input("Enter a string: ")
ans=palindrome_locator(s)
print(ans)