"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('my_file.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n')
with open('new_file.txt', 'w', encoding='utf-8') as new_f:
    new_f.write('\n'.join(content[1:]))
with open('new_file.txt', 'r', encoding='utf-8') as new_f:
    lines = 0
    for line in new_f:
        lines += 1
    print('Строк в файле -', lines)
with open('new_file.txt', 'r', encoding='utf-8') as new_f:
    my_list = (new_f.read().split('\n'))
    for i in range(len(my_list)):
        print('Слов в строке', i + 1, '-', len(my_list[i].split()))
