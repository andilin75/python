'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

with open('test.txt', 'r', encoding='utf-8') as f:
    list_number = f.read()
    list_number = list_number.replace('One', 'Один')
    list_number = list_number.replace('Two', 'Два')
    list_number = list_number.replace('Three', 'Три')
    list_number = list_number.replace('Four', 'Четыре')
with open('rus.txt', 'w', encoding='utf-8') as rf:
    rf.write(list_number)
