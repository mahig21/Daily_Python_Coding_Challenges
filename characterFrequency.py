#12-05-26
#Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.
def get_frequency(s):
    set_freq={}
    for i in s:
        charCount=s.count(i)
        set_freq[i]=charCount
    return set_freq
s=input("Enter a string: ")
set_freq=get_frequency(s)
print(set_freq)