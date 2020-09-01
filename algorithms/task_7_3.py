# *********************************************************************************************************
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).
# **********************************************************************************************************

import random

M = random.randint(0, 20)
SIZE = M * 2 + 1
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def median_search(array):
    for i in range(0, len(array)):
        left = 0
        right = 0
        equally = 0
        for j in range(0, len(array)):
            if array[i] == array[j]:
                equally += 1
            elif array[i] > array[j]:
                left += 1
            else:
                right += 1
            if equally > len(array) / 2:
                median = array[i]
                break
        if ((left + equally) > len(array) / 2) and ((right + equally) > len(array) / 2):
            median = array[i]
            break
    return median


print(median_search(array))
