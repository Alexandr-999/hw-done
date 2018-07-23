import os


def make_folder(name, path='./'):
    try:
        os.mkdir(path + name)
        print('Создано успешно')
    except Exception:
        print('Не удалось создать')


def rm_folder(path):
    try:
        os.rmdir(path)
        print('Удалено успешно')
    except Exception:
        print('Не удалось удалить')


def list_cur_dir(path=os.curdir):
    for i in os.listdir(path):
        print(i)


def change_dir(name):
    try:
        os.chdir(name)
        print('Теперь мы в дире:', os.path.abspath(os.curdir))
    except Exception:
        print('Не удалось перейти')

# list_cur_dir()
