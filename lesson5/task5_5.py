'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('test_2.txt', 'w') as f:
    f.write('1 2 3 4 5')
with open('test_2.txt', 'r') as f:
    list_numbers = f.read().split()
    sum_number = 0
    for i in range(len(list_numbers)):
        sum_number = sum_number + float(list_numbers[i])
print('Сумма чисел в файле: ', sum_number)
