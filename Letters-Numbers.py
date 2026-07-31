#29-01-26
#Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
def separate_letters_and_numbers(s):
    newS=""
    flag=0
    for i in range(len(s)-1):
        newS+=s[i]
        if flag==1 and s[i+1].isalpha():
            flag=0
            newS+="-"
        if s[i+1].isdigit() and s[i].isalpha():
            newS+="-"
            flag=1
    return newS+s[-1]

s=input("Enter a string containing only letters and numbers: ")
print(separate_letters_and_numbers(s))