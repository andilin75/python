a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = 1.1
i = 2
while True:
    a = a * c
    if a >= b:
        print(i)
        break
    else:
        i += 1
