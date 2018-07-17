# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
import datetime

print('___________________________')


def summary_str(name, age, city, first_login='NEWER', *args, **kwargs):
    print(
        f'{name}, возраст: {age}, проживает в {city}. Дополнительно: {list(map(str, args))}. \nStatus: {kwargs} \nFirst login: {first_login}')


summary_str('Василий', '15', 'Москва', 'a long time ago', 'ADDITIONAL INFO', 'some other info',
            level=1, health=100, armor=0, alive=True,
            online_since=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print('___________________________')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_numbers(*args):
    return max(args)


print(max_numbers(111, 35, 99))

print('___________________________')


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_len_on_str(*args):
    return max(args, key=len)


print(max_len_on_str('Hello, world!', '15', '143', 'min'))
