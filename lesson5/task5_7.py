"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""

import json

with open('firms.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n')
    names = [content[i].split(' ')[0] for i in range(len(content))]
    profits = [(int(content[i].split(' ')[2]) - int(content[i].split(' ')[3])) for i in range(len(content))]
    average_profit = sum([el for el in profits if el > 0]) / (len([el for el in profits if el > 0]))
    result_list = [dict(zip(names, profits)), {'average profit': average_profit}]
with open('result.json', 'w', encoding='utf-8') as f_write:
    json.dump(result_list, f_write)
