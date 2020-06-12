"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д"""


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        new_mylist = [' '.join(map(str, self.my_list[i])) for i in range(len(self.my_list))]
        return ('\n'.join(map(str, new_mylist)))

    def __add__(self, other):
        result_matrix = [[0, 0], [0, 0], [0, 0]]
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[0])):
                result_matrix[i][j] = self.my_list[i][j] + other.my_list[i][j]
        result_matrix = [' '.join(map(str, result_matrix[i])) for i in range(len(result_matrix))]
        return ('\n'.join(map(str, result_matrix)))


m = Matrix([[31, 22], [37, 43], [51, 86]])
m2 = Matrix([[10, 10], [10, 10], [10, 10]])

print(m)
print(m2)
print(m + m2)