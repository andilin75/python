# *****************************************************************************
# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.
# *****************************************************************************

# https://drive.google.com/file/d/1IKILQ4Tfy6gtK-dDEkCi--CaubFAOWYU/view?usp=sharing

print('Введите координаты двух точек')
x1 = float(input('Первая точка, координата x: '))
y1 = float(input('Первая точка, координата y: '))
x2 = float(input('Вторая точка, координата x: '))
y2 = float(input('Вторая точка, координата y: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'y = {k}x + {b}')