# вход >> данные от пользователя: номер, название, цена, количество и единица измерения товара
# выход >> структура "Товары" - список кортежей из 2 элементов - номера товара и словаря с другими параметрами
# сбор аналитики о товарах - реализация словаря {ключ: параметр товара, значение: список значений параметров}

products = []
want_add = 'да'
while want_add == 'да':
    want_add = input('Если хотите добавить товар в список введите "да", иначе введите "нет" ')
    if want_add == 'да':
        number = int(input('Введите номер товара: '))
        name = input('Введите название товара: ')
        price = int(input('Введите цену товара: '))
        quantity = int(input('Введите количество товара: '))
        unit = input('Введите единицу измерения товара: ')
        product = (number, {'название': name, 'цена': price, 'количество': quantity, 'ед': unit})
        products.append(product)
for product in products:
    print(product)
# собираем аналитику
names = []
prices = []
quantityes = []
units = []
for product in products:
    names.append((product[1])['название'])
    prices.append((product[1])['цена'])
    quantityes.append((product[1])['количество'])
    units.append((product[1])['ед'])
analytics = {
    'название': list(set(names)),
    'цена': list(set(prices)),
    'количество': list(set(quantityes)),
    'ед': list(set(units))
}
print(analytics)

