#21-06-26
"""
Given a word or sentence, return a corrected version where every word
follows the "I before E except after C" rule.

- If a word contains "ei" not preceded by "c", replace it with "ie".
- If a word contains "ie" preceded by "c", replace it with "ei".
- All other words are left unchanged.
"""
def i_before_e(sentence):
    newSent=""
    flag=0
    for i in range(len(sentence)-1):
        if flag==1:
            flag=0
            continue
        if sentence[i]=='e' and sentence[i+1]=='i' and sentence[i-1]!='c':
            newSent+="ie"
            flag=1
        elif sentence[i]=='i' and sentence[i+1]=='e' and sentence[i-1]=='c':
            newSent+="ei"
            flag=1
        else:
            newSent+=sentence[i]
            flag=0
    return newSent+sentence[-1]
sentence=input("Enter a word or sentence: ")
newSent=i_before_e(sentence)
print(newSent)