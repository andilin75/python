# *********************************************************************************************************
# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# **********************************************************************************************************

# Урок 3. Задание 4
# *********************************************************************************************************
# Определить, какое число в массиве встречается чаще всего.
# *********************************************************************************************************

import random, timeit, cProfile

SIZE = 1600
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Вариант 1

def max_count_number_1(array):
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
    return x


#print (timeit.timeit('max_count_number_1(array)', number=1000, globals=globals()))
# SIZE = 100 0.7565123
# SIZE = 200 2.2438926
# SIZE = 400 5.5245106999999996
# SIZE = 800 12.719594
# SIZE = 1600 28.5016614

#cProfile.run('max_count_number_1(array)')
# SIZE = 100  1    0.001    0.001    0.001    0.001 task_4_1_1.py:23(max_count_number_1)
# SIZE = 200  1    0.002    0.002    0.002    0.002 task_4_1_1.py:23(max_count_number_1)
# SIZE = 400  1    0.005    0.005    0.005    0.005 task_4_1_1.py:23(max_count_number_1)
# SIZE = 800  1    0.013    0.013    0.013    0.013 task_4_1_1.py:23(max_count_number_1)
# SIZE = 1600 1    0.025    0.025    0.025    0.025 task_4_1_1.py:23(max_count_number_1)

# Вариант 2

def max_count_number_2(array):
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
    return x


#print (timeit.timeit('max_count_number_2(array)', number=1000, globals=globals()))
# SIZE = 100 1.6309335
# SIZE = 200 5.610443999999999
# SIZE = 400 22.3328431
# SIZE = 800 94.1125701
# SIZE = 1600 370.3480807

#cProfile.run('max_count_number_2(array)')
# SIZE = 100  1    0.003    0.003    0.003    0.003 task_4_1_1.py:57(max_count_number_2)
# SIZE = 200  1    0.003    0.003    0.003    0.003 task_4_1_1.py:57(max_count_number_2)
# SIZE = 400  1    0.028    0.028    0.028    0.028 task_4_1_1.py:57(max_count_number_2)
# SIZE = 800  1    0.094    0.094    0.094    0.094 task_4_1_1.py:57(max_count_number_2)
# SIZE = 1600 1    0.403    0.403    0.404    0.404 task_4_1_1.py:57(max_count_number_2)

# Вариант 3

def max_count_number_3(array):
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
    return x


#print (timeit.timeit('max_count_number_3(array)', number=1000, globals=globals()))
# SIZE = 100 0.08981430000000001
# SIZE = 200 0.08984539999999999
# SIZE = 400 0.2023905
# SIZE = 800 0.41990460000000007
# SIZE = 1600 0.8257285999999999

#cProfile.run('max_count_number_3(array)')
# SIZE = 100  1    0.000    0.000    0.000    0.000 task_4_1_1.py:87(max_count_number_3)
# SIZE = 200  1    0.000    0.000    0.000    0.000 task_4_1_1.py:87(max_count_number_3)
# SIZE = 400  1    0.000    0.000    0.000    0.000 task_4_1_1.py:87(max_count_number_3)
# SIZE = 800  1    0.000    0.000    0.000    0.000 task_4_1_1.py:87(max_count_number_3)
# SIZE = 1600 1    0.002    0.002    0.002    0.002 task_4_1_1.py:87(max_count_number_3)

# ВЫВОДЫ:
# 1-й вариант - скорость низкая, сложность линейная O(1,25*n)
# 2-й вариант - худший по скорости, квадратичная сложность O(n^2) из-за вложенного цикла
# 3-й вариант - лучший вариант, сложность линейная O(n)
