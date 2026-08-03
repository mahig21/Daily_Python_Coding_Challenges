#16-01-26
"""
Given two positive integers representing the lengths for the two legs (the two short 
sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg 
lengths together and then taking the square root of that total (a² + b² = c²).
"""
import math
def is_integer_hypotenuse(a, b):
    hypo_sqaure=(a*a)+(b*b)
    hypo=str(math.sqrt(hypo_sqaure))
    if ".0" in hypo:
        return True
    return False
print(is_integer_hypotenuse(3, 4))