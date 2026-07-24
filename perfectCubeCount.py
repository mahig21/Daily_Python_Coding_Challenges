#03-03-26
"""
Given two integers, determine how many perfect cubes exist in the range
between and including the two numbers.

- The lower number is not guaranteed to be the first argument.
- A number is a perfect cube if there exists an integer (n) where 
  n * n * n = number. For example, 27 is a perfect cube because 
  3 * 3 * 3 = 27.
"""
def count_perfect_cubes(a, b):
    count=0
    if a<b:
        small=a
        large=b
    else:
        small=b
        large=a
    for i in range(-100,100):
        cube=i*i*i
        if cube>=small and cube<=large:
            count+=1
    return count
count=count_perfect_cubes(3,30)
print(count)