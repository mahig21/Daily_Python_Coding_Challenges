#05-05-26
"""
    Given a positive integer, determine whether it is a narcissistic number.
    
    A number is narcissistic if the sum of each of its digits raised to the 
    power of the total number of digits equals the number itself.
    """
import math
def is_narcissistic(n):
    new_num=0
    original_num=n
    digits=0
    while(n!=0):
        digits+=1
        n=math.floor(n/10)
    n=original_num
    while(n!=0):
        rem=n%10
        new_num+=rem**digits
        n=math.floor(n/10)
    if new_num==original_num:
        return True
    else:
        return False
ans=is_narcissistic(9474)
print(ans)