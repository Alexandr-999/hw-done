import os


def make_folder(path, name):
    os.mkdir(path + name)


for i in range(1, 10):
    make_folder('./', 'dir_' + str(i))
    print(os.path.curdir)
