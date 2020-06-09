"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт."""

from itertools import cycle


class TrafficLight:
    __color = []

    def __init__(self, color_1, color_2, color_3):
        self.__color = [color_1, color_2, color_3]

    def running(self, green_duration):
        duration = [7, 2, green_duration]
        mode = dict(zip(self.__color, duration))
        i = 0
        for el in cycle(mode):
            if i > 10:
                break
            else:
                try:
                    if self.__color != ['red', 'yellow', 'green']:
                        raise Exception('Неверный порядок режимов')
                except Exception as e:
                    print(e)
                    break
                print(el, mode[el])
                i += 1


t = TrafficLight('red', 'yellow', 'green')
t.running(6)
