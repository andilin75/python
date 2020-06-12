"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes():
    @abstractmethod
    def consumption_tissue(self, size, height):
        self.size = size
        self.height = height
        coat_tissue = round((self.size / 6.5 + 0.5), 2)
        suit_tissue = round((2 * self.height + 0.3), 2)

        return coat_tissue + suit_tissue


class Coat(Clothes):
    def consumption_tissue(self, size, heiht=None):
        return round((size / 6.5 + 0.5), 2)


class Suit(Clothes):
    def consumption_tissue(self, size=None, height=None):
        return round((2 * height + 0.3), 2)


clothes = Clothes()
coat = Coat()
suit = Suit()
print(coat.consumption_tissue(54))
print(suit.consumption_tissue(height=180))
print(clothes.consumption_tissue(54, 180))
