import os


def rm_folder(path):
    os.rmdir(path)


for i in list(os.walk('./'))[0][1]:
    if 'dir' in i:
        rm_folder(i)

