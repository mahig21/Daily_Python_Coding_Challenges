#17-01-26
"""
Finds the indices of two unique numbers in an array that add up to a given target.

Args:
    nums (list): An array of numbers to search through.
    target (int): The target sum value.

Returns:
    list or str: An array containing the two indices in ascending order if a valid 
                 pair is found. Returns the string "Target not found" if no two 
                 numbers sum up to the target.
"""
def find_target(arr, target):
    target_index=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                target_index.append(i)
                target_index.append(j)
                return target_index
    return "Target not found"
print(find_target([1, 3, 5, 6, 7, 8], 15))