#25-02-26
"""
Calculates the differences between consecutive numbers in an array.

Given an array of numbers, this function returns a new array containing 
the value needed to get from each number to the next number.

Rules:
- The difference is calculated as the next number minus the current number.
- For the last number in the array, the value is 0 since there is no next number.

Example:
    Input: [1, 2, 4, 7]
    Returns: [1, 2, 3, 0]
"""
def find_differences(arr):
    diff=[]
    for i in range(len(arr)-1):
        diff.append(arr[i+1]-arr[i])
    diff.append(0)
    return diff
arr=input("Enter an array of numbers separated by commas: ")
arr=[int(x) for x in arr.split(",")]
diff=find_differences(arr)
print(diff)