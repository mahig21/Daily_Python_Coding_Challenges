#01-09-26
"""
The Tribonacci sequence is a series of numbers where each number is the sum of the
three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the
sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an
integer representing the length of the sequence, return an array containing the
sequence of the given length.

- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.
"""
def tribonacci_sequence(start_sequence, length):
    a=start_sequence[0]
    b=start_sequence[1]
    c=start_sequence[2]
    if length<=3:
        return start_sequence[:length]
    else:
        for i in range(length-3):
            summ=a+b+c
            start_sequence.append(summ)
            a=b
            b=c
            c=summ
        return start_sequence
start_sequence=input("Enter the first three numbers of a Tribonacci sequence (comma-separated): ")
start_sequence=[int(x) for x in start_sequence.split(",")]  
length=int(input("Enter the length of the sequence: "))
print(tribonacci_sequence(start_sequence, length))
