#28-08-26
"""
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

1. The second most expensive laptop if it is within your budget, or
2. The most expensive laptop that is within your budget, or
3. 0 if no laptops are within your budget.

* Duplicate prices should be ignored.
"""
def get_laptop_cost(laptops, budget):
    if min(laptops)>budget:
        return 0
    for i in range(1,len(laptops)):
        if laptops[-2]<=budget:
            return laptops[-2]

laptops=input("Enter the prices of laptops separated by commas: ")
laptops=[int(i) for i in laptops.split(",")]
budget=int(input("Enter your budget: "))
print(get_laptop_cost(laptops, budget))