#16-03-36
#Given two integers, determine if you can evenly divide the first one by the second one.
def is_evenly_divisible(a, b):
    if (a%b)==0:
        return True
    return False
ans=is_evenly_divisible(3186, 9)
print(ans)