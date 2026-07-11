#01-07-26
"""
Given a string of a person's first and last name, calculate their lucky number using the following rules:
- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number
- If the final value is zero (0), return 13.
"""
def getVowelConsonant(word):
    word=word.lower()
    vow=0
    con=0
    for char in word:
        if char in 'aeiou':
            vow+=1
        else:
            con+=1
    return vow,con
def get_large(a,b):
    if a>b:
        return a
    else:
        return b
def get_small(a,b):
    if a<b:
        return a
    else:
        return b
def get_lucky_number(name):
    name=name.split()
    first_name=name[0]
    last_name=name[1]
    len1=len(first_name)
    len2=len(last_name)
    vow1,con1=getVowelConsonant(first_name)
    vow2,con2=getVowelConsonant(last_name)
    large=get_large(len1,len2)*get_large(vow1,vow2)*get_large(con1,con2)
    small=get_small(len1,len2)*get_small(vow1,vow2)*get_small(con1,con2)
    lucky_num=large-small
    if lucky_num==0:
        return 13
    else:
        return lucky_num
    

lucky_num=get_lucky_number("Chloe Perez")
print(lucky_num)