#07-07-26
#Given two integers, round the first to the nearest multiple of the second.
def round_to_nearest_multiple(num, multiple):
    mul_list=[]
    difference=100
    for i in range(1,11):
        mul_list.append(i*multiple)
    for i in mul_list:
        diff=abs(num-i)
        if diff<=difference:
            difference=diff
            ans=i
        else:
            return ans
m=int(input("Enter the number: "))
n=int(input("Enter the multiple: "))
ans=round_to_nearest_multiple(m, n)
print(ans)