#01-03-26
#Given an array, determine if it is flat.
# -An array is flat if none of its elements are arrays.
def is_flat(arr):
    for i in arr:
        type_i=type(i)
        if type_i==type([1,2]):
            return False
    return True
ans=is_flat([1, [2, 3], 4])
print(ans)