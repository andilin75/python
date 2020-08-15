# *********************************************************************************************************
# Определить, какое число в массиве встречается чаще всего.
# **********************************************************************************************************

import random

SIZE = 1000
MIN_ITEM = -70
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_count = 0
x = None
i = 0

while i < len(array):
    a = array[i]
    count_number = 0
    for j in array:
        if j == a:
            count_number += 1
            if count_number > max_count:
                max_count = count_number
                x = j
            i += 1

print(f'{x} - {max_count} раз')
