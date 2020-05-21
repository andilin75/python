# вход >> рейтинг - не возрастающий набор натуральных чисел (задается непосредственно в коде)
# пользователь вводит новый элемент рейтинга
# выход >> рейтинг с новым элементом
# если существуют элементы с одинаковым значением, то новый элемент размещается после них

my_list = [7, 5, 3, 3, 2]
new_rate = int(input('Введите рейтинг: '))
if my_list.count(new_rate) == 0:
    my_list.append(new_rate)
    my_list = sorted(my_list, reverse=True)
else:
    i = my_list.index(new_rate) + my_list.count(new_rate)
    my_list.insert(i, new_rate)
print(my_list)
