# ******************************************************************************
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# ******************************************************************************

# https://drive.google.com/file/d/1IKILQ4Tfy6gtK-dDEkCi--CaubFAOWYU/view?usp=sharing

x = int(input('Введите целое число от 100 до 999: '))

a = x // 100
b = (x % 100) // 10
c = (x % 100) % 10

print(f'Сумма {a + b + c}, Произведение {a * b * c}')