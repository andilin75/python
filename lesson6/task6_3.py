"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""

class Worker:
    name = ()
    surname = ()
    position = ()
    _income = {'wage', 'bonus'}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print('Полное имя: {} {}'.format(self.name, self.surname))

    def get_total_income(self):
        print('доход - {}'.format(self._income['wage'] + self._income['bonus']))


w = Position('Вася', 'Пупкин', 'инженер', 35000, 40000)
print(w.name, w.surname, w.position, w._income)
w.get_full_name()
w.get_total_income()
