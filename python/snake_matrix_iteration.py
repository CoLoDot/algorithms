#! /usr/bin/env python
def snake_iteration(matrix):
    row, col, max_row, max_col = 0, 0, len(matrix)-1, len(matrix)-1
    result = []

    while col <= max_col:
        if col % 2 == 0:
            result += [matrix[i][col] for i in range(row, max_row + 1)]
            col += 1
        elif col % 2 != 0:
            result += [matrix[i][col] for i in range(max_row, row - 1, -1)]
            col += 1
    return result


matrix = [
    [1, 8, 9, 16],
    [2, 7, 10, 15],
    [3, 6, 11, 14],
    [4, 5, 12, 13]
]

print(snake_iteration(matrix=matrix))
# should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
