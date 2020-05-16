number = input('Введите число: ')
i = 0
result = 0
while i < len(number):
    next_number = int(number[i])
    if next_number > result:
        result = int(number[i])
    else:
        i += 1
print(result)
