#06-09-26
"""
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it.
For instance, given [[1, 2], [3, 4]], which looks like this:

| 1 | 2 |
| 3 | 4 |

You should return [[3, 1], [4, 2]], which looks like this:

| 3 | 1 |
| 4 | 2 |
"""
def rotate(matrix):
    rotated_matrix=[]
    for i in range(len(matrix[0])):
        matrix_row=[]
        for j in matrix:
            matrix_row.append(j[i])
        rotated_matrix.append(matrix_row[::-1])
    return rotated_matrix

matrix = input("Enter a matrix (e.g. [[1, 2], [3, 4]]): ")
matrix = eval(matrix)
print(rotate(matrix))