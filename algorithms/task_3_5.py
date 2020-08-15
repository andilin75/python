# *********************************************************************************************************
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
# **********************************************************************************************************

import random

SIZE = 100
MIN_ITEM = -70
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
x = 0
j = 0

for i in array:
    if i < 0:
        if x == 0 or i > x:
            x = i
            pos = j
    j += 1

if x == 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Число {x}, индекс {pos}')
