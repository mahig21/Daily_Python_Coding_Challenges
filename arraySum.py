#09-03-26
#Given an array of numbers, return the sum of all the numbers.
def sum_array(numbers):
    summ=sum(numbers)
    return summ
numbers=input("Enter list of numbers separated by commas: ").split(",")
numbers=[int(i) for i in numbers]
summ=sum_array(numbers)
print(summ)