#15-04-26
"""
Given an array of integers, return a new array using the following rules:
1. Sort the integers in ascending order
2. Then swap all values whose index is a multiple of 3 with the value before it.
"""
def sort_and_swap(arr):
    arr.sort()
    swap_arr=[]
    flag=0
    for i in range(len(arr)-1):
        if flag==1:
            flag=0
            continue
        if (i+1)%3==0:
            swap_arr.append(arr[i+1])
            swap_arr.append(arr[i])
            flag=1
        else:
            swap_arr.append(arr[i])
    swap_arr.append(arr[-1])
    return swap_arr
swap_array=sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8])
print(swap_array)