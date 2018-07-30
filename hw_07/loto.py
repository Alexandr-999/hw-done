"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:



--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Card:
    def __init__(self, username):
        self.username = username
        self.card_done = []
        self.card = ''
        if username:
            self._fill_card()

    def _fill_card(self):
        c = random.sample(range(1, 91), 27)
        line1 = c[0:9]
        line1.sort()
        line2 = c[9:18]
        line2.sort()
        line3 = c[18:]
        line3.sort()
        x = 0
        while x < 3:
            r1 = random.sample(range(0, 9), 4)
            r2 = random.sample(range(0, 9), 4)
            r3 = random.sample(range(0, 9), 4)
            for i in r1:
                line1[i] = '-'
                x += 1
            for i in r2:
                line2[i] = '-'
                x += 1
            for i in r3:
                line3[i] = '-'
                x += 1
            self.card_done = line1, line2, line3
            self.user_card()

    def user_card(self):
        print('---Карта игрока ' + self.username)
        self.card = "\t\n".join('\t' + "\t".join(map(str, l)) for l in self.card_done) + '\t'
        print(self.card)
        print()


class Game:

    def start_game(self):
        bag = list(random.sample(range(1, 91), 90))
        print(bag)
        i = 0
        round_count = 1
        formatted_card_1 = user_card.card
        formatted_card_2 = pc_card.card
        while True:
            keg = bag[i]
            print(f'Раунд: {round_count}, в игре {user_card.username} и {pc_card.username} \n'
                  f'ТЯНЕМ БОЧОНОК! и выпадает номер = {keg}')
            if (str(keg) + '') in user_card.card.split():
                print(f'У игрока {user_card.username} найдено совпадение! Зачеркиваем?')
                answer = input('Y or N?')
                if answer == 'Y':
                    formatted_card_1 = formatted_card_1.replace(('\t' + str(keg) + '\t'), '\tX\t')
                    print(formatted_card_1)
                elif answer == 'N':
                    print('Game over потому что логика задания совершенно глупая')
                    break
                else:
                    print('Надо было отвечать Y или N :(')
                    break

            if (str(keg) + '') in pc_card.card.split():
                print(f'У игрока {pc_card.username} найдено совпадение!')
                formatted_card_2 = formatted_card_2.replace(('\t' + str(keg) + '\t'), '\tX\t')
                print(formatted_card_2)
            round_count += 1
            i += 1
            if formatted_card_1.count('X') == 15:
                print(f'Победил - {user_card.username}!!!')
                print(f'Карточка {user_card.username} - \n'
                      f'{formatted_card_1}')
                print(f'Карточка {pc_card.username} - \n'
                      f'{formatted_card_2}')
                print('В мешке остались: ', bag[i:])
                break
            if formatted_card_2.count('X') == 15:
                print(f'Победил - {pc_card.username}!!!')
                print(f'Карточка {pc_card.username} - \n'
                      f'{formatted_card_2}')
                print(f'Карточка {user_card.username} - \n'
                      f'{formatted_card_1}')
                print('В мешке остались: ', bag[i:])
                break


user_card = Card('Gamer')

pc_card = Card('PC')

game = Game
game.start_game('')
