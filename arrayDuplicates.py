#30-08-26
"""
Given an array of integers, return an array of integers that appear more than once in 
the initial array, sorted in ascending order. If no values appear more than once, return 
an empty array.

- Only include one instance of each value in the returned array.
"""
def find_duplicates(arr):
    duplicates=[]
    for i in arr:
        if arr.count(i)!=1:
            if i not in duplicates:
                duplicates.append(i)
    duplicates.sort()
    return duplicates
print(find_duplicates([1, 2, 3, 4, 1, 2]))
