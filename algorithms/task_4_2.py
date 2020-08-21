# *********************************************************************************************************
# Написать два алгоритма нахождения i-го по счёту простого числа.
#  - Без использования Решета Эратосфена;
#  - Использовать алгоритм решето Эратосфена
# **********************************************************************************************************

import timeit, cProfile

# Вариант 1. Без использования Решета Эратосфена.

def prime_num(i):
    prime_numbers = [2]
    n = 2
    while i != len(prime_numbers):
        n += 1
        count_ = 0
        for j in range(2, n):
            if n % j == 0:
                count_ = 1
                break
        if count_ == 0:
            prime_numbers.append(n)
    return prime_numbers[-1]


# print (timeit.timeit('prime_num(10)', number=1000, globals=globals())) # 0.08330680000000001
# print (timeit.timeit('prime_num(20)', number=1000, globals=globals())) # 0.17171229999999998
# print (timeit.timeit('prime_num(40)', number=1000, globals=globals())) # 0.6584863
# print (timeit.timeit('prime_num(80)', number=1000, globals=globals())) # 3.1024379
# print (timeit.timeit('prime_num(160)', number=1000, globals=globals())) # 14.029143799999998

# cProfile.run('prime_num(10)')
# # 1    0.000    0.000    0.000    0.000 task_4_2.py:11(prime_num)
# cProfile.run('prime_num(20)')
# # 1    0.000    0.000    0.000    0.000 task_4_2.py:11(prime_num)
# cProfile.run('prime_num(40)')
# # 1    0.001    0.001    0.001    0.001 task_4_2.py:11(prime_num)
# cProfile.run('prime_num(80)')
# # 1    0.003    0.003    0.003    0.003 task_4_2.py:11(prime_num)
# cProfile.run('prime_num(160)')
# # 1    0.014    0.014    0.015    0.015 task_4_2.py:11(prime_num)

# Вариант 2. Использовать алгоритм решето Эратосфена

def prime_num_2(i):
    n = round(i * 61.153)  # Если верить википедии этого коэффициента достаточно для поиска 16*10^24 простых чисел
    numbers = [j for j in range(n)]
    numbers[1] = 0
    for j in range(2, n):
        if numbers[j] != 0:
            k = j + j
            while k < n:
                numbers[k] = 0
                k += j
    result = [j for j in numbers if j != 0]
    return result[i - 1]


# print (timeit.timeit('prime_num_2(10)', number=1000, globals=globals())) # 0.5300426
# print (timeit.timeit('prime_num_2(20)', number=1000, globals=globals())) # 1.0676923
# print (timeit.timeit('prime_num_2(40)', number=1000, globals=globals())) # 2.5953291
# print (timeit.timeit('prime_num_2(80)', number=1000, globals=globals())) # 4.8372112000000005
# print (timeit.timeit('prime_num_2(160)', number=1000, globals=globals())) # 9.813782

# cProfile.run('prime_num_2(10)')
# #         1    0.001    0.001    0.001    0.001 task_4_2.py:45(prime_num_2)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:47(<listcomp>)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:55(<listcomp>)
# cProfile.run('prime_num_2(20)')
# #         1    0.002    0.002    0.002    0.002 task_4_2.py:45(prime_num_2)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:47(<listcomp>)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:55(<listcomp>)
# cProfile.run('prime_num_2(40)')
# #         1    0.001    0.001    0.002    0.002 task_4_2.py:45(prime_num_2)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:47(<listcomp>)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:55(<listcomp>)
# cProfile.run('prime_num_2(80)')
# #         1    0.007    0.007    0.008    0.008 task_4_2.py:45(prime_num_2)
# #         1    0.000    0.000    0.000    0.000 task_4_2.py:47(<listcomp>)
# #         1    0.001    0.001    0.001    0.001 task_4_2.py:55(<listcomp>)
# cProfile.run('prime_num_2(160)')
# #         1    0.015    0.015    0.020    0.020 task_4_2.py:45(prime_num_2)
# #         1    0.002    0.002    0.002    0.002 task_4_2.py:47(<listcomp>)
# #         1    0.003    0.003    0.003    0.003 task_4_2.py:55(<listcomp>)

#ВЫВОД: Функция с решетом лучше, так как проще, сложность линейная O(n).
# В функции без решета сложность квадратичная, время растет быстрее с увеличением порядкового номера числа.
