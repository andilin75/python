revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if revenue == costs:
    print('Вы сработали в 0')
elif revenue < costs:
    print('Ваш убыток:', costs - revenue)
else:
    profit = revenue - costs
    print('Ваша прибыль: ', profit)
    profitability = profit / revenue
    print(type(profitability))
    strenght = int(input('Введите численность сотрудников: '))
    performance = profitability / strenght
