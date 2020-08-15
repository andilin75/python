# *********************************************************************************************************
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# **********************************************************************************************************

import random

SIZE = 10
MIN_ITEM = -700
MAX_ITEM = 100000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_number = array[0]
min_number = array[0]
j = -1

for i in array:
    j += 1
    if i > max_number:
        max_number = i
        pos_max = j
    elif i < min_number:
        min_number = i
        pos_min = j

array[pos_max], array[pos_min] = array[pos_min], array[pos_max]

print(array)
