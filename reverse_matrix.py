"""
3. Reverse Bidimensional Matrix

Given a bidimensional matrix, reverse each row independently.

Return the modified matrix.

Example:

Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
"""

matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]
]


def reverser(matrix: list[list[int]]) -> list[list[int]]:
    for row in matrix:
        row.reverse()
    return matrix


rev_matrix = reverser(matrix)
for row in rev_matrix:
    print(row)