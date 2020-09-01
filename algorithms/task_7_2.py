# *********************************************************************************************************
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
# **********************************************************************************************************

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        left = merge_sort(array[:(len(array) // 2)])
        right = merge_sort(array[(len(array) // 2):])
        return merge(left, right)


print(merge_sort(array))
