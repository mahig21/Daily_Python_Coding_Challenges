#04-07-26
"""
    Given a 4-digit number, return the number of times you need to apply 
    Kaprekar's routine until reaching 6174.
    
    Kaprekar's routine works as follows:
    - Arrange the digits in descending order to form the largest number
    - Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
    - Subtract the smaller from the larger
    - Repeat with the new number
    """
def kaprekar(n,count=0):
    if n==6174:
        return count
    list_a=[]
    count+=1
    str1=str(n)
    for i in str1:
        list_a+=[i]
    list_a.sort()
    list_b=list_a[::-1]
    n1="".join(list_a)
    n2="".join(list_b)
    n=abs(int(n1)-int(n2))
    return kaprekar(n,count)

n=int(input("Enter a 4-digit number: "))
count=kaprekar(n)
print(count)