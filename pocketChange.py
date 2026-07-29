#05-02-26
"""
Given an array of integers representing the coins in your pocket, with each
integer being the value of a coin in cents, return the total amount in the
format "$D.CC".

- 100 cents equals 1 dollar.
- In the return value, include a leading zero for amounts less than one
  dollar and always exactly two digits for the cents.
"""
def count_change(change):
    summ=sum(change)/100
    return f"${summ:.2f}"

print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))