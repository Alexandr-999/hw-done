# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
root = [1, 2, 4, 0]
new = [i**2 for i in root]
print(new)


print('___________________________')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['apple', 'orange', 'apricot']
fruits_2 = ['apple', 'banana', 'apricot', 'dragonfruit']
same = [i for i in fruits_2 if i in fruits_1]
print(same)

print('___________________________')


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

list = [random.randint(-1000, 1000) for _ in range(0, 30)]
list_res = [i for i in list if i >= 0 and i % 3 == 0 and i % 4 != 0]
print(list)
print(list_res)
