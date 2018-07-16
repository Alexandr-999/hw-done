# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.


# вычислите и выведите y
import math

equation = 'y = -12x + 11111140.2121'

lst = equation.split(' ')
print(lst)

x = 2.5
y = 0
k_tmp = []
k = ''
b = lst[len(lst)-1]
parsed_num_oper = str(lst[2])
for i in parsed_num_oper:
    if i.isdigit():
        k_tmp.append(i)
    if i == '-':
        k += i

k += str(k_tmp[0]) + str(k_tmp[len(k_tmp)-1])
print(k)

y = float(k) * float(x) + float(b)
print(y)

print('#########################################################')
print()

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
date = '-2.12.1001'
err_count = 0
days_in_m = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
t_lst = date.split('.')
# print(t_lst)
for i in t_lst:
    if len(t_lst[0]) != 2 or len(t_lst[1]) != 2 or len(t_lst[-1]) != 4 or int(t_lst[-1]) > 9999:
        print('err found! len or year')
        err_count += 1
        break
    elif not i.isnumeric():
        print('err isdigit:', i)
        err_count += 1
if t_lst[1] in days_in_m:
    if int(t_lst[0]) > days_in_m[t_lst[1]]:
        print('err. Too much days in month :|')
else:
    print('err. Month not found')
    err_count += 1

if err_count == 0:
    print('Great! Date accepted')
else:
    print(err_count, 'Errors found!')

print('#########################################################')
print()

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
# 51  52  53  54  55        |  5       | 15
# 46  47  48  49  50        |  5       | 14
# 41  42  43  44  45        |  5       | 13
# 36  37  38  39  40        |  5       | 12
# 31  32  33  34  35        |  5       | 11
#   27  28  29  30          |   4      | 10
#   23  24  25  26          |   4      | 9
#   19  20  21  22          |   4      | 8
#   15  16  17  18          |   4      | 7
#     12  13  14            |  3       | 6
#     9   10  11            |  3       | 5
#     6   7   8             |  3       | 4
#       4   5               |   2      | 3
#       2   3               |   2      | 2
#         1                 |  1       | 1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


x = int(input('x ='))
limit = 20000000
last_room_in_block = 0
full_list = []
last_floor = 0
first_floor = 0
stop = 0
first_room_bf = 0
last_room_bf = 0
fb = 0
first_room_in_block = 0
rooms_in_block = 0
block = 0

for i in range(limit):
    if stop == 0:
        full_list.append(i)
        last_room_in_block = i * i + last_room_in_block
        first_room_in_block = last_room_in_block - (full_list[-1] ** 2) + 1
        last_floor = last_floor + full_list[-1]
        first_floor = last_floor - (full_list[-1] - 1)
        rooms_in_block = full_list[-1] ** 2
        block = full_list[-1]
        # print('block =', block)
        print('floors in block =', block)
        # print('rooms in block =', rooms_in_block)
        # print('first_room_in_block =', first_room_in_block)
        # print('last_room_in_block =', last_room_in_block)
        # print('first floor on block =', first_floor)
        # print('last floor on block =', last_floor)
        print()
        while first_room_in_block < x < last_room_in_block and stop == 0:
            stop = 1
            print()
            break
room_list = []
b_f = 0
fl = 0
for i in range(first_room_in_block, last_room_in_block + 1, block):
    b_f += 1
    if i <= x < i + block:
        fl = i
        break
floor_res = first_floor + (b_f - 1)
print('FLOOR =', floor_res)
print(fl)
from_left = (x - fl + 1)
print('FROM LEFT =', from_left)



