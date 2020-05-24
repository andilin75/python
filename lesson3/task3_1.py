"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль"""


def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        error = ('На ноль делить нельзя!')
        return error
    return result


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
print(division(a, b))
