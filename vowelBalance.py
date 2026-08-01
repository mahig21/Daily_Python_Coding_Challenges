#11-08-26
"""
Determines whether the number of vowels in the first half of a string 
is equal to the number of vowels in the second half.

Rules:
- Vowels are defined as 'a', 'e', 'i', 'o', and 'u' (case-insensitive).
- The string can contain any type of characters.
- If the string has an odd number of characters, the center character is ignored.
"""
def is_balanced(s):
    vow="aeiou"
    mid=len(s)//2
    first_half=s[:mid]
    if len(s)%2==0:
        second_half=s[mid:]
    else:
        second_half=s[mid+1:]
    vow1=0
    vow2=0
    for i in first_half:
        if i.lower() in vow:
            vow1+=1
    for i in second_half:
        if i.lower() in vow:
            vow2+=1
    if vow1==vow2:
        return True
    return False

print(is_balanced("Lorem Ipsum"))
