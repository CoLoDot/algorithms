#! /usr/bin/env python
def anticlockwise_iteration(matrix):
    top, left = 0, 0
    right, bottom = len(matrix) - 1, len(matrix) - 1
    direction = 0
    result = []

    while (top <= bottom) and (left <= right):
        if direction == 0:
            result += [matrix[top][i] for i in range(right, left - 1, -1)]
            top += 1
            direction = 1
        elif direction == 1:
            result += [matrix[i][left] for i in range(top, bottom + 1)]
            left += 1
            direction = 2
        elif direction == 2:
            result += [matrix[bottom][i] for i in range(left, right + 1)]
            bottom -= 1
            direction = 3
        elif direction == 3:
            result += [matrix[i][right] for i in range(bottom, top - 1, -1)]
            right -= 1
            direction = 0
    return result


matrix = [
    [3, 2, 1],
    [4, 9, 8],
    [5, 6, 7],
]

print(anticlockwise_iteration(matrix=matrix))
# should return [1, 2, 3, 4, 5, 6, 7, 8, 9]
