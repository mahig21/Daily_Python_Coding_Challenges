#12-08-26
"""
Given a string representing a number, and an integer base from 2 to 36, determine
whether the number is valid in that base.

- The string may contain integers, and uppercase or lowercase characters.
- The check should be case-insensitive.
- The base can be any number 2-36.
- A number is valid if every character is a valid digit in the given base.
- Example of valid digits for bases:
    - Base 2: 0-1
    - Base 8: 0-7
    - Base 10: 0-9
    - Base 16: 0-9 and A-F
    - Base 36: 0-9 and A-Z
"""
def is_valid_number(n, base):
    for i in n:
        if i.isdigit():
            if int(i)>=base:
                return False
        if base==16:
            if i.isalpha():
                if not (str(i).upper()>='A' and str(i).upper()<='F'):
                    return False
        if base==36:
            if i.isalpha():
                if not (str(i).upper()>='A' and str(i).upper()<='Z'):
                    return False
        if base==2 or base==8 or base==10:
            if i.isalpha():
                return False
            
    return True

print(is_valid_number("ABC", 16))