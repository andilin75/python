# *********************************************************************************************************
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке
# Примечание: в сумму не включаем пустую строку и строку целиком.
# **********************************************************************************************************

import hashlib


def sub_counting(my_str):
    my_set = set()
    empty_str = hashlib.sha1(my_str[0:0].encode('utf-8')).hexdigest()
    whole_str = hashlib.sha1(my_str.encode('utf-8')).hexdigest()
    for i in range(len(my_str)):
        for j in range(i, len(my_str)):
            if hashlib.sha1(my_str[i:j + 1].encode('utf-8')).hexdigest() == empty_str or hashlib.sha1(
                    my_str[i:j + 1].encode('utf-8')).hexdigest() == whole_str:
                continue
            else:
                my_set.add(hashlib.sha1(my_str[i:j + 1].encode('utf-8')).hexdigest())
    return len(my_set)


print(sub_counting('papa'))
