"""Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

with open('my_file.txt', 'w', encoding='utf-8') as f:
    user_input = None
    while user_input != (''):
        user_input = (input('Введите данные: '))
        print(user_input, file=f)
    print('Ввод данных окончен')
