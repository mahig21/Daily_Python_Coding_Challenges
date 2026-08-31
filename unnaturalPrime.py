#23-08-26
"""
Given an integer, determine if that number is a prime number or a negative prime
number.

- A prime number is a positive integer greater than 1 that is only divisible by 1 and
  itself.
- A negative prime number is the negative version of a positive prime number.
- 1 and 0 are not considered prime numbers.
"""
def is_unnatural_prime(n):
    n=abs(n)
    if n==0 or n==1:
        return False
    flag=0
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            flag=1
            return False
    if flag==0:
        return True
n=int(input("Enter an integer: "))
print(is_unnatural_prime(n))