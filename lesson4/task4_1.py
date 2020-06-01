"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

try:
    script_name, hours_worked, hour_rate, prize = argv
except ValueError:
    print('Введите через пробел отработанные часы, часовую ставку и размер премии')


def payroll_prep(hours_worked, hour_rate, prize):
    try:
        payroll = float(hours_worked) * float(hour_rate) + float(prize)
    except ValueError:
        print('Это должны быть числа')
    else:
        print('Заработная плата: ', payroll)


payroll_prep(hours_worked, hour_rate, prize)
