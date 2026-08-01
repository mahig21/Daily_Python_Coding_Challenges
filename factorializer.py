#18-08-26
#Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.
#The factorial of zero is 1.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter an integer from 0 to 20: "))
print(factorial(n))