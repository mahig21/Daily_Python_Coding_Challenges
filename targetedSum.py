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
arr=input("Enter an array of numbers separated by commas: ").split(",")
arr=[int(i) for i in arr]   
target=int(input("Enter the target sum: "))
print(find_target(arr, target))