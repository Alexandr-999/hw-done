# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, damage, armor):
        return damage * random.uniform(0, damage) // armor * random.uniform(0, armor)

    def _attack(self, who_attack, who_defend):
        damage = self.calculate_damage(who_attack.damage, who_defend.armor)
        who_defend.hp -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage,
                                                                        who_defend.hp))

    # def incoming_attack(self, dmg):
    #     self.hp = self.hp - dmg


class Player(Person):
    pass


class Enemy(Person):
    pass


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_game(self, player, enemy):
        # Запоминаем кто последний атаковал
        last_attacker = player
        while player.hp > 0 and enemy.hp > 0:
            if last_attacker == player:
                player._attack(enemy, player)
                last_attacker = enemy
            else:
                player._attack(player, enemy)
                last_attacker = player
        if player.hp > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


player1 = Player('I AM!', 100, 5, 0.44)
player2 = Enemy('Htlr', 100, 5, 0.46)

print(player1.name, player2.name)

battle = Battle(player1, player2)
battle.start_game(player1, player2)

