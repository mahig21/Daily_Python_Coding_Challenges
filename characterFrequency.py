#12-05-26
#Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears.
def get_frequency(s):
    set_freq={}
    for i in s:
        charCount=s.count(i)
        set_freq[i]=charCount
    return set_freq
set_freq=get_frequency("mississippi")
print(set_freq)