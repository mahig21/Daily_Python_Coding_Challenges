def find_differences(arr):
    diff=[]
    for i in range(len(arr)-1):
        diff.append(arr[i+1]-arr[i])
    diff.append(0)
    return diff
diff=find_differences([10, 15, 19, 22, 24, 25])
print(diff)