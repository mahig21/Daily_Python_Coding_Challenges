#09-09-26
"""Given a string, determine if all the characters in the string are unique.
-Uppercase and lowercase letters should be considered different characters."""

def all_unique(s):
    for i in s:
        if s.count(i)!=1:
            return False
    return True
print(all_unique("QwErTy123!@"))

