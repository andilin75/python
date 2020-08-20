'''Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

with open('my_file.txt', 'r', encoding='utf-8') as f:
    my_list = f.read().split('\n')
    low_paid = [my_list[i].split(' ')[0] for i in range(len(my_list)) if float(my_list[i].split(' ')[1]) < 20000]
    print('Сотрудники с окладом менее 20 тыс: ', ', '.join(low_paid))

    salaries = 0
    for i in range(len(my_list)):
        salaries = salaries + float(my_list[i].split(' ')[1])
    print('Средняя величина дохода сотрудников: ', round(salaries / (len(my_list)), 2))
