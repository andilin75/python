"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:
    speed = ()
    color = ()
    name = ()
    is_police = bool()

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула {}'.format(direction))

    def show_speed(self, current_speed):
        print('Текущая скорость {}'.format(current_speed))


class TownCar(Car):
    def car_in_traffic(self):
        print('Машина в пробке')

    def show_speed(self, current_speed):
        if current_speed > 60:
            print('Текущая скорость {}. Превышение скорости'.format(current_speed))
        else:
            print('Текущая скорость {}'.format(current_speed))


class SportCar(Car):
    def acceleration(self, acceleration):
        print('Разгон до 100 км/ч за {} секунд'.format(acceleration))


class WorkCar(Car):
    def loading_car(self):
        print('Машина погружена')

    def show_speed(self, current_speed):
        if current_speed > 40:
            print('Текущая скорость {}. Превышение скорости'.format(current_speed))
        else:
            print('Текущая скорость {}'.format(current_speed))


class PoliceCar(Car):
    def warning_shot(self):
        print('Выстрел в воздух')


tc = TownCar(70, 'красный', 'Москвич', False)
sc = SportCar(120, 'черный', 'Волга', True)
wc = WorkCar(60, 'белый', 'КАМАЗ', False)
pc = PoliceCar(60, 'синий', 'УАЗ', True)

print(tc.speed, tc.color, tc.name, tc.speed)
print(sc.speed, sc.color, sc.name, sc.speed)
print(wc.speed, wc.color, wc.name, wc.speed)
print(pc.speed, pc.color, pc.name, pc.speed)

tc.go()
sc.stop()
wc.turn('направо')
pc.show_speed(10)

tc.car_in_traffic()
tc.show_speed(80)
sc.acceleration(8)
wc.loading_car()
wc.show_speed(40)
pc.warning_shot()
