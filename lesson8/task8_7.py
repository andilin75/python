"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        return '({}+{}j)'.format((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return '({}+{}j)'.format((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(5, 10)

print(z1 + z2)
print(z1 * z2)

z3 = complex(1, 2)  # Проверка
z4 = complex(5, 10)
print(z3 + z4)
print(z3 * z4)
