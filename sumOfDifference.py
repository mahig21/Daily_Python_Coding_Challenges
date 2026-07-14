#26-05-26
#Given an array of numbers, return the sum of the differences between each number and the one that follows it.
def sum_of_differences(arr):
    sumOfDiff=0
    for i in range(len(arr)-1):
        difference=arr[i+1]-arr[i]
        sumOfDiff+=difference
    return sumOfDiff
arr=input("Enter the array of numbers separated by spaces: ").split()
arr=[int(num) for num in arr]
sumOfDiff=sum_of_differences(arr)
print(sumOfDiff)