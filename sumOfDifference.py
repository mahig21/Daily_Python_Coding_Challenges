#26-05-26
#Given an array of numbers, return the sum of the differences between each number and the one that follows it.
def sum_of_differences(arr):
    sumOfDiff=0
    for i in range(len(arr)-1):
        difference=arr[i+1]-arr[i]
        sumOfDiff+=difference
    return sumOfDiff
sumOfDiff=sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7])
print(sumOfDiff)