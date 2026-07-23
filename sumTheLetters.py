#02-03-26
"""
Given a string, return the sum of its letters.

- Letters are A-Z in uppercase or lowercase
- Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
- Uppercase and lowercase letters have the same value.
- Ignore all non-letter characters.
"""
def sum_letters(s):
    sum1=0
    for i in s:
        if i.isalpha():
            sum1+=ord(i.upper())-64
    return sum1
s=input("Enter a string: ")
sum1=sum_letters(s)
print(sum1)