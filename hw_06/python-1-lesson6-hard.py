# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


# class Purchase


# class Paint


# class Sewing

class Storage:
    def __init__(self, count_paint=0, count_cloth=0, count_yum=0):
        self.count_paint = count_paint
        self.count_cloth = count_cloth
        self.count_yum = count_yum
        print(self.get_stat())  # почему тут при выполнении вылезает None совершенно непонятно

    def add_paint(self, count):
        try:
            if count > 0:
                self.count_paint += count
                self.get_stat()
        except Exception:
            print('Some error')

    def add_cloth(self, count):
        try:
            if count > 0:
                self.count_cloth += count
                self.get_stat()
        except Exception:
            print('Some error')

    def add_yum(self, count):
        try:
            if count > 0:
                self.count_yum += count
                self.get_stat()
        except Exception:
            print('Some error')

    def get_paint(self):
        return self.count_paint

    def get_cloth(self):
        return self.count_cloth

    def get_yum(self):
        return self.count_yum

    def get_stat(self):  # не ясно как вызывать стату каждый раз без обращения к методу
        print(f'У вас на складе:'
              f' {self.count_paint} литров краски,'
              f' {self.count_cloth} метров ткани,'
              f' {self.count_yum} метров нитей.')


class BuildToy:
    def __init__(self, toy_name, toy_type='None', toy_size='None', toy_color='blank'):
        self.toy_name = toy_name
        self.toy_type = toy_type
        self.toy_size = toy_size
        self.toy_color = toy_color


    def get_toy(self):
        print(f'Name = {self.toy_name}, type = {self.toy_type}, size = {self.toy_size}, color = {self.toy_color}')

    def process_toy(self, type):
        types = ['Bear', 'Rabbit', 'Fry']
        if type in types:  # непонятно как обратиться к родителю без использования имени переменной (storage)
            if type == 'Bear':
                BuildToyBear(self.toy_name, '10', '10')
        else:
            print('Не найден такой тип игрушки. Возможные варианты:', types)


class BuildToyBear:
    def __init__(self, name, cloth_used, paint_used):
        self.name = name
        self.cloth_used = cloth_used
        self.paint_used = paint_used

# тут у меня кончилось время и я доделать не успею :(


storage = Storage()
storage.add_paint(int(input('Сколько краски вы привезли? :')))
storage.add_cloth(int(input('Сколько ткани вы привезли? :')))
storage.add_yum(int(input('Сколько нитей вы привезли? :')))

build = BuildToy(123, 'Bear', 'small', 'red')
build.get_toy()
build.process_toy('Bear')

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
