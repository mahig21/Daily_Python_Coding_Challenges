#27-07-26
#Given a number, determine whether it is a pronic number.
#A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.
def is_pronic(n):
    for i in range(n+1):
        if i*(i+1)==n:
            return True
    return False
ans=is_pronic(int(input("Enter a number: ")))
print(ans)