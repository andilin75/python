"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class Warehouse:
    def __init__(self):
        office_equipment = []
        self.office_equipment = office_equipment

    def reception(self, **kwargs):
        self.office_equipment.append({**kwargs})
        return (self.office_equipment)

    def transfer(self, position_number):
        return self.office_equipment.pop(position_number)


class OfficeEquipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class OwnEror(Exception):
    def __init__(self, txt):
        self.txt = txt


class Printer(OfficeEquipment):
    def __init__(self, name, model, print_speed):
        super().__init__(name, model)
        self.print_speed = print_speed

    def departure(self):
        try:
            self.quantity = input('Введите количество: ')
            if self.quantity.isdigit() == False:
                raise OwnEror('Вы ввели не число')
        except OwnEror as e:
            print(e)
        else:
            return w.reception(name=self.name, model=self.model, print_speed=self.print_speed,
                               quantity=int(self.quantity))


class Scanner(OfficeEquipment):
    def __init__(self, name, model, light_sorce):
        super().__init__(name, model)
        self.light_sorce = light_sorce

    def departure(self):
        try:
            self.quantity = input('Введите количество: ')
            if self.quantity.isdigit() == False:
                raise OwnEror('Вы ввели не число')
        except OwnEror as e:
            print(e)
        else:
            return w.reception(name=self.name, model=self.model, light_sorce=self.light_sorce,
                               quantity=int(self.quantity))


class Xerox(OfficeEquipment):
    def __init__(self, name, model, print_resolution):
        super().__init__(name, model)
        self.print_resolution = print_resolution

    def departure(self):
        try:
            self.quantity = input('Введите количество: ')
            if self.quantity.isdigit() == False:
                raise OwnEror('Вы ввели не число')
        except OwnEror as e:
            print(e)
        else:
            return w.reception(name=self.name, model=self.model, print_resolution=self.print_resolution,
                               quantity=int(self.quantity))


class Subdivision:
    pass


class EconomicDepartment(Subdivision):
    def reception(self, number_position):
        office_equipment = []
        self.office_equipment = office_equipment
        self.number_position = int(number_position)
        office_equipment.append(w.transfer(self.number_position))


class HRDepartment(Subdivision):
    pass


w = Warehouse()
p = Printer('Принтер', 'Brother', 150)
s = Scanner('Сканер', 'HP', 52)
x = Xerox('Ксерокс', 'Xerox', 50)
ed = EconomicDepartment()

print(p.departure())
ed.reception(0)
print(w.office_equipment)
print(ed.office_equipment)
