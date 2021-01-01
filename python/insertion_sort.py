#! /usr/bin/env python

def insertion_sort_increasing(arr):
    array = arr
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key

    return array


def insertion_sort_decreasing(arr):
    array = arr
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] < key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key

    return array


arr_1 = [5, 2, 4, 6, 1, 3]
arr_2 = [31, 41, 59, 26, 41, 58]

print('\ninsertion_sort_increasing')
print(insertion_sort_increasing(arr=arr_1))
print(insertion_sort_increasing(arr=arr_2))
print('\ninsertion_sort_decreasing')
print(insertion_sort_decreasing(arr=arr_1))
print(insertion_sort_decreasing(arr=arr_2))
