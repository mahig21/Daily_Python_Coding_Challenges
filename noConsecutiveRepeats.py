#23-03-26
#Given a string, determine if it has no repeating characters.
#A string has no repeats if it does not have the same character two or more times in a row.

def has_no_repeats(s):
    words=s.split()
    for i in words:
        set_a=set(i)
        if len(i)!=len(set_a):
            return False
    return True
ans=has_no_repeats("freeCodeCamp")
print(ans)