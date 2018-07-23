# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   #cp <file_name> - создает копию указанного файла
#   #rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   #cd <full_path or relative_path> - меняет текущую директорию на указанную
#   #ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# --------------------------------------------------------------

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def list_cur_dir(path=os.curdir):  # добавил заодно вывод списка файлов, а то ls это не pwd
    for i in os.listdir(path):
        print(i)
    print('Мы в дире:', os.path.abspath(os.curdir))


def change_dir():
    try:
        os.chdir(dir_name)
        print('Теперь мы в дире:', os.path.abspath(os.curdir))
    except Exception:
        print('Не удалось перейти')


def copy_file():
    try:
        shutil.copy(file_name, file_name + '_copy')
        print("Done")
    except Exception:
        print('Не удалось скопировать')


def remove_file():
    try:
        answer = input('Да или нет?:')
        if answer == 'Да':
            os.remove(file_name)
            print("OK")
        else:
            print('Ответ не принят')
    except Exception:
        print("Не удалось удалить файл")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": list_cur_dir,
    "cd": change_dir,
    "cp": copy_file,
    "rm": remove_file
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
