# вход >> пользователь вводит месяц в виде целого числа от 1 до 12
# выход >> сообщение о том к какому времени года относится месяц
# решения через list и через dict

month = int(input('Введите месяц: '))
# решение через list:
seasons_list = ['', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень',
                'зима']
print(seasons_list[month])
# решение через dict:
seasons_dict = {
    1: 'зима', 2: 'зима', 12: 'зима',
    3: 'весна', 4: 'весна', 5: 'весна',
    6: 'лето', 7: 'лето', 8: 'лето',
    9: 'осень', 10: 'осень', 11: 'осень'
}
print(seasons_dict.get(month))
