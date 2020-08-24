# *********************************************************************************************************
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
# **********************************************************************************************************

from collections import Counter

number_company = int(input('Введите количество предприятий: '))
enterprises = {}
total_profit = 0

for i in range(1, number_company + 1):
    profit = 0
    name = input('Введите наименование предприятия: ')
    quarter_profit_1 = int(input('Введите прибыль за 1 квартал: '))
    quarter_profit_2 = int(input('Введите прибыль за 2 квартал: '))
    quarter_profit_3 = int(input('Введите прибыль за 3 квартал: '))
    quarter_profit_4 = int(input('Введите прибыль за 4 квартал: '))
    profit = quarter_profit_1 + quarter_profit_2 + quarter_profit_3 + quarter_profit_4
    enterprises[name] = profit
    total_profit += profit

count_ = 0
for key in enterprises:
    if enterprises[key] >= total_profit / number_company:
        count_ += 1

enterprises = Counter(enterprises)

print(f'Средняя прибыль = {round(total_profit / number_company, 2)}')
print(f'Предприятия, прибыль которых больше или равна средней: {enterprises.most_common(count_)}')
print(f'Предприятия, прибыль которых меньше средней: {enterprises.most_common()[:-(number_company + 1 - count_):-1]}')
