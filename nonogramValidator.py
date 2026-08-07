#07-08-26
"""
Given an array of clue numbers and an array of cells, determine whether the cells 
satisfy the nonogram clue.

- The clue is an array of numbers representing the lengths of consecutive filled 
  cells, in order. For example, a clue of [3, 2] means there should be 3 
  consecutive filled cells followed by 2 consecutive filled cells, separated by at 
  least one empty cell.
- The row is an array of 1s (filled) and 0s (empty).
"""
def is_valid_nonogram(clue, cells):
    newClue=[]
    countt=0
    for i in cells:
        if i==0 and countt!=0:
            newClue.append(countt)
            countt=0
        elif i==1:
            countt+=1
    if countt!=0:
        newClue.append(countt)
    return (newClue==clue)
clue=input("Enter the clue numbers separated by spaces: ").split()
cells=input("Enter the cells (1 for filled, 0 for empty) separated by spaces: ").split()
clue = [int(x) for x in clue]
cells = [int(x) for x in cells]
print(is_valid_nonogram(clue, cells))