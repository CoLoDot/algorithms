#! /usr/bin/env python

def insertion_sort_matrix(matrix):
    for x in range(0, len(matrix)):
        cur = matrix[x]
        for i in range(1, len(cur)):
            k = cur[i]
            p = i - 1
            while p >= 0 and cur[p] > k:
                cur[p + 1] = cur[p]
                p = p - 1
            cur[p + 1] = k
    return matrix


matrix = [[0, 2, 89, 1], [999, 675, 23, 44],
          [12, 78, 23, 90], [23, 67, 12, 8]]

print(insertion_sort_matrix(matrix))
