#30-04-26
"""
Given a character, determine if its 8-bit binary representation can be found 
in the following grid, horizontally or vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0

For example, "A" has the binary representation 01000001, which 
appears in the first row from left to right.
"""
crossword = [
  [0, 1, 0, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 1, 1, 1, 1],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 0, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 0],
  [0, 1, 1, 0, 1, 0, 0, 0],
  [1, 0, 1, 0, 1, 1, 1, 0]
]

def is_in_crossword(char):
    target_ascii = ord(char)
    size = len(crossword)
    
    for i in range(size):
        row = crossword[i]
        col = [crossword[j][i] for j in range(size)]
        sequences = [
            row,        
            row[::-1],  
            col,        
            col[::-1]   
        ]
        
        for seq in sequences:
            decimal_value = int("".join(map(str, seq)), 2)
            if decimal_value == target_ascii:
                return True
                
    return False

char = input("Enter a character to check in the crossword: ")
ans = is_in_crossword(char)
print(ans)