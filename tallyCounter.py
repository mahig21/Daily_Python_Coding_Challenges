#13-07-26
"""
Given a string of tally marks, return the total count represented.
Each pipe "|" represents one count.
Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
Groups are separated by a space.
"""
def get_tally_count(s):
    count=0
    for i in s:
        if i=="|" or i=="/":
            count+=1
    return count

count=get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |") 
print(count)