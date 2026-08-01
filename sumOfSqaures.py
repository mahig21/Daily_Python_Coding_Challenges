#19-08-26
#Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.
def sum_of_squares(n):
    summ=0
    for i in range(1,n+1):
        summ+=i*i
    return summ
print(sum_of_squares(10))