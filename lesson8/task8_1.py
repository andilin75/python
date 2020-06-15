"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def conversion_type(cls, date_str):
        return int(date_str[:2]), int(date_str[3:5]), int(date_str[6:])

    @staticmethod
    def date_validation(date_str):
        try:
            if int(date_str[:2]) < 1 or int(date_str[:2]) > 31 or int(date_str[3:5]) < 1 or int(
                    date_str[3:5]) > 12 or int(date_str[6:]) < 0 or int(date_str[6:]) > 9999:
                raise ValueError('Неверная дата')
        except ValueError as e:
            return e
        else:
            return 'Всё хорошо'


print(Date.conversion_type('21-06-1975'))
print(Date.date_validation('14-06-2020'))

