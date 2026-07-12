#30-06-26
# Given two strings, return a count of characters from the second string that can be found in the first.
# Duplicate characters in the second string are counted separately.
def duplicate_character_count(str1, str2):
    count=0
    set_a=set(str1)
    for i in set_a:
        alphacount=str2.count(i)
        if alphacount!=0:
            count+=alphacount
    return count

count=duplicate_character_count("jambo", "bonjour")
print(count)