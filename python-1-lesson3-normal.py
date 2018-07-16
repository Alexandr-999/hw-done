# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html

import os


def save_to_file(x, path, file):
    pathfile = path + file
    for k, v in x.items():  # для всех пар ключ - значение в x
        res = f'{k} - {v}\n'  # создаем переменную
        with open(pathfile, 'a', encoding='UTF-8') as f:  # безопасно открываем файл на append
            f.write(res)  # пишем в файл
    return 200  # status code

path = './'
file = '1.txt'
names = ['SOUL', 'HaizenberG', 'mike', 'Boss']
price = [42000, 500000, 15000, 100]

names_price = dict(zip(names, price))

if save_to_file(names_price, path, file) == 200:
    print('OK: File successfully written')
    print('----')
else:
    print('Shit happens')  # можно еще добавить проверку что name==string, price==int

dict_from_file = {}
with open(path + file, 'rt', encoding='UTF-8') as f:
    for line in f:
        nalog = line.split()
        if int(nalog[-1]) <= 50000:
            print(str(nalog[0]).title() + ': salary(' + nalog[-1] + ') -13% =', int(nalog[-1]) - (int(nalog[-1]) / 100 * 13))

