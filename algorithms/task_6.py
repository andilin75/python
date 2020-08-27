# *********************************************************************************************************
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# **********************************************************************************************************

import random, sys


def items_var(cont):
    if isinstance(cont, str):
        return (25 + len(cont))
    elif isinstance(cont, int):
        if cont == 0:
            return 12
        else:
            return 14
    elif isinstance(cont, float):
        return 16


def allocated_memory(*vars):
    result = 0
    for var in [*vars]:
        result += sys.getsizeof(var)
        if hasattr(var, '__iter__'):
            if hasattr(var, 'items'):
                for key, value in var.items():
                    result += (items_var(key) + items_var(value))
            elif not isinstance(var, str):
                for item in var:
                    result += items_var(item)
    return result


# Урок 3. Задание 4
# *********************************************************************************************************
# Определить, какое число в массиве встречается чаще всего.
# *********************************************************************************************************

SIZE = 1600
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# Вариант 1

max_count = 0
x = None
i = 0
while i < len(array):
    count_number = 0
    for j in array:
        if j == array[i]:
            count_number += 1
            if count_number > max_count:
                max_count = count_number
                x = j
            i += 1
print(x)
print(f'Размер в байтах: {allocated_memory(max_count, x, i, array, count_number, j)}')
# Python 3.8.2 Windows10 x32
# Результат -> Размер в байтах: 28956

# Вариант 2

x = array[0]
max_count = 1
for i in range(len(array)):
    count_number = 1
    for j in range(i + 1, len(array)):
        if array[j] == array[i]:
            count_number += 1
    if count_number > max_count:
        max_count = count_number
        x = array[i]
print(x)

print(f'Размер в байтах: {allocated_memory(x, array, max_count, i, count_number, j)}')
# Результат -> Размер в байтах: 28956

# Вариант 3

my_dict = {}
max_count = 1
x = None
for i in array:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
    if my_dict[i] > max_count:
        max_count = my_dict[i]
        x = i
print(x)

print(f'Размер в байтах: {allocated_memory(my_dict, max_count, x, i, array)}')
# Результат -> Размер в байтах: 39730

# ВЫВОДЫ:
# Наибольший объем памяти (39730 байт) выделяется под переменные в варианте 3 из-за наличия словаря.
# Варианты 1 и 2 одинаковы (28956 байт)
# При этом вариант 3 будет работать быстрее, благодаря применению словаря. Поэтому оптимальный вариант зависит от
# того, что в приоритете - скорость выполнения (тогда вариант 3) или выделяемая память (тогда вариант 1, т.к. он чуть
# быстрее варианта 2 при одинаковой выделяемой памяти)
