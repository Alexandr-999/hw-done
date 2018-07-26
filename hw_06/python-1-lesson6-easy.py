# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class Car:
    def __init__(self, speed, name, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.color

    def go(self):
        print('В движении')

    def stop(self):
        print('Остановка')

    def turn(self, direction):
        if direction == 'left':
            print('Повернули налево')
        elif direction == 'right':
            print('Повернули направо')
        else:
            print('не повернули')


class TownCar(Car):
    def comfort(self, comfort=100):
        print(comfort)

    def stereo_sound(self):
        print('TADAM')


class SportCar(Car):
    def sport(self, turbo=True):
        print('Turbo =', turbo)


class WorkCar(TownCar):
    def seats(self, seats=6):
        print('seats =', seats)


class PoliceCar(Car):
    def set_police(self):
        self.is_police = True


car1 = WorkCar(100, 'NameOfMyCar', 'Black')
print(car1.turn('right'))

car2 = PoliceCar(200, 'SHERIFF', 'White', True)
print(car2.get_color(), car2.is_police)




# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
