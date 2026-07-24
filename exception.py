"""
Given two integers A and B.
Write a program to print the result of A divided by B.
"""
digits = input("Enter two numbers separated by a space: ").split()
nums=[]
for i in digits:
    if i.isdigit():
        nums+=[int(i)]
    else:
        nums+=[i]
try:
    ans = nums[0]/nums[1]
    print(ans)
except ZeroDivisionError:
    print("Denominator can't be 0")
except TypeError:
    print("Input should be an integer")
    

