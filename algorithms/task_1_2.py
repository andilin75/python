# ***********************************************************************************
# Определить, является ли год, который ввел пользователем, високосным или не високосным.
#************************************************************************************

# https://drive.google.com/file/d/1IKILQ4Tfy6gtK-dDEkCi--CaubFAOWYU/view?usp=sharing

x = int(input('Введите год: '))

if x % 400 == 0:
    print('Високосный год')
elif x % 100 == 0:
    print('Невисокосный год')
elif x % 4 == 0:
    print('Високосный год')
else:
    print('Невисокосный год')