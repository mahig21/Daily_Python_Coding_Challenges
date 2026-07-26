#15-03-26
"""
Captured Chess Pieces

Given an array of strings representing chess pieces you still have on the board, 
calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece   | Abbreviation | Quantity | Value
--------|--------------|----------|-------
Pawn    | "P"          | 8        | 1
Rook    | "R"          | 2        | 5
Knight  | "N"          | 2        | 3
Bishop  | "B"          | 2        | 3
Queen   | "Q"          | 1        | 9
King    | "K"          | 1        | 0

Rules:
- The given array will only contain the abbreviations above.
- Any of the 16 pieces not included in the given array have been captured.
- Return the total value of all captured pieces, unless...
- If the King has been captured, return "Checkmate".
"""
chess={
    'P':(8,1),
    'R':(2,5),
    'N':(2,3),
    'B':(2,3),
    'Q':(1,9),
    'K':(1,0),
}
def get_captured_value(pieces):
    if 'K' not in pieces:
        return "Checkmate"
    pieceSet={'P','R','N','B','Q','K'}
    points=0
    for i in pieceSet:
        countt=pieces.count(i)
        points+=(chess[i][0]-countt)*chess[i][1]
    return points
pieces=input("Enter the chess pieces you still have on the board separated by spaces: ").split()
ans=get_captured_value(pieces)
print(ans)