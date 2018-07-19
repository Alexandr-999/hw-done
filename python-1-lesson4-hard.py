# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

import re


person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:  # == сработает только в случае ввода именно той суммы которая есть на счету. Изменено на >= так как можно снять денег столько чтобы на счету сотался 0
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:  # str to int потому что input всегда возвращает string а в def start() мы переводим значения в int
        print(check_account(person))
    elif choice == 2:
        count = input('Сумма к снятию:')
        if check_is_digit(count):
            count = float(count)
            print(withdraw_money(person, count))


def start():
    card_number = ''
    pin_code = ''
    try:  # проверяем на ошибку если введено только одно значение для .split
        card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
    except ValueError:
        print('ERROR! Something strange happened! Try one more time')
    card_pin = str(f'{card_number} {pin_code}')
    if re.match(pattern_card_pin, card_pin):
        card_number = int(card_number)
        pin_code = int(pin_code)
        person = get_person_by_card(card_number)
        if person and is_pin_valid(person, pin_code):
            while True:
                choice = int(input('Выберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор:'))

                if choice == int(3):
                    print('До свидания!')
                    break
                process_user_choice(choice, person)
        else:
            print('Номер карты или пин код введены неверно!')  #неверно в данном случае пишется слитно, так как нет отрицания/противопоставления!
    else:
        print('Ошибка при вводе данных!')
        start()


def check_is_digit(*args):  #проверяем что цифры а не буквы
    for i in args:
        if not i.isdigit() and '.' not in i:
            print('Пожалуйста введите правильный формат данных!')
        elif i == '.':
            print('Пожалуйста введите правильный формат данных!')
        else:
            return True


pattern_card_pin = '^(\d{16})\s\d{4}$'
pattern_choice = '^\d{1}$'

start()
