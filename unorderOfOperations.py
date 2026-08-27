#27-08-26
"""
Given an array of integers and an array of string operators, apply the operations to
the numbers sequentially from left-to-right. Repeat the operations as needed until all
numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of
evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of
operations.

* Valid operators are +, -, *, /, and %.
"""
def calculate(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    elif op=='%':
        return num1%num2
def evaluate(numbers, operators):
    ans=0
    opIndex=0
    fNum=numbers[0]
    for i in range(len(numbers)-1):
        ans=calculate(fNum,numbers[i+1],operators[opIndex])
        fNum=ans
        if opIndex==len(operators)-1:
            opIndex=0
        else:
            opIndex+=1
    return ans
numbers=[int(x) for x in input("Enter the numbers separated by spaces: ").split()]
operators=input("Enter the operators separated by spaces: ").split()
print(evaluate(numbers, operators))