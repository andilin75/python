"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

with open('sessions.txt', 'r', encoding='utf-8') as f:
    sum_hours = []
    while True:
        sessions = f.readline()
        if sessions != '':
            for lines in sessions:
                hours_list = []
                hours = ' '
                for char in sessions:
                    if char.isdigit():
                        hours = hours + char
                    else:
                        if hours != ' ':
                            hours_list.append(int(hours))
                            hours = ' '
                if hours != ' ':
                    hours_list.append(int(hours))
        else:
            break
        sum_hours.append(sum(hours_list))

with open('sessions.txt', 'r', encoding='utf-8') as f:
    sessions = f.read().split('\n')
    subjects = [sessions[i].split()[0] for i in range(len(sessions))]
print(dict(zip(subjects, sum_hours)))
