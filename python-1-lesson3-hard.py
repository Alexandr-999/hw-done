# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
import random


def attack(person1_name, person1_hp, person1_armor, person2_name, person2_dmg):
    res = person1_hp - damage(person2_dmg, person1_armor)
    print(f'\n{person1_name}: HP = {person1_hp} | Armor = {person1_armor} \n\n'
          f'{person2_name} basic damage = {person2_dmg} | HP = {person1_hp} \n'
          f'...BATTLE!.. \n')
    print(f'{person1_name}: HP = {res}\n'
          f'____________________________________________________')
    return res


def damage(dmg, arm):
    return dmg / arm


player_name = input('Please, enter a Name for your avatar: ')

player_params = {'name': player_name,
                 'health': 100,
                 'armor': 1.2,
                 'damage': 50 + random.randint(-10, 10),
                 'damage_bonus': 0,
                 'level': 1
                 }

enemy_params = {'name': 'Enemy_' + str(random.randint(0, 100)),
                'health': 100,
                'armor': 1,
                'damage': 50 + random.randint(-10, 10),
                'damage_bonus': 0
                }

while player_params.get('health') >= 0.0 and enemy_params.get('health') >= 0.0:
    player_params.update({'health': attack(player_params.get('name'),
                                           player_params.get('health'),
                                           player_params.get('armor'),
                                           enemy_params.get('name'),
                                           enemy_params.get('damage')
                                           )})
    enemy_params.update({'health': attack(enemy_params.get('name'),
                                          enemy_params.get('health'),
                                          enemy_params.get('armor'),
                                          player_params.get('name'),
                                          player_params.get('damage')
                                          )})

print(player_params.get('health'), enemy_params.get('health'))

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
