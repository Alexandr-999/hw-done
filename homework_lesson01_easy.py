# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Task - 1:')

one = 1  # int()
two = 'two' # string()
three = True # bool()
four = False
five = 5.0  # float()
six = one * 6
seven = five + (1 * 2)  # float()
eight = int(input('Enter 8 pleeease: '))  # str() to int
nine = int(five) + int(five) - one  # float() to int()
ten = 50 / five  # float()

while eight != 8:
    eight = int(input('Enter 8 please: '))
print(
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten
)

print('int(True)=', int(three))
print('int(False)=', int(four))

print('----')
print('Task - 2')

n_from_user = input('Please enter a random number: ')
# print(type(n_from_user))
# надо как-то проверить что мы не пытаемся сконвертировать букву в число..
if n_from_user.isdigit():  # .isdigit проверяет число ли там или нет, и для этого не нужно конвертить в int!
    print(n_from_user, '+ 2 =', int(n_from_user) + 2)
elif ' ' in n_from_user:  # .проверка на содержится ли символ пробела в строке
    print('You never know result of | _SPACE(biggest keyboard button, not a space around nowhere)_ + 2 | :(')
else:
    print('You never know result of |', n_from_user, '+ 2 | :(')
    print('You die! We wait for a number! Game over now!')

print('----')
print('Task - 3')

# ну тут я пропустил проверки на int и пробелы, так как выше уже понял.
# На них надо функцию(def) писать и проверять.
# Ну а в первом задании я не допер еще до этого :)
age = input('How old are you? ')
if int(age) >= 18:
    print("Access granted! You're so old!")
else:
    print('Access denied. Wait some years:', 18 - int(age))
