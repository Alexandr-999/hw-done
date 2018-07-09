# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому

# пациент в хорошем состоянии,
# если ему до 30 лет и вес от 50 и до 120 кг,

# Пациенту требуется начать вести правильный образ жизни,
# если ему более 30 и вес меньше 50 или больше 120 кг

# Пациенту требуется врачебный осмотр,
# если ему более 40 и вес менее 50 или больше 120 кг.

# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)

# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print("Hi! I'm a Doctor AiBolit! Tell me about yourself please: ")

w_min = 50
w_max = 120

while True:
    name = input("Name please: ")
    sname = input("Surname please: ")
    age = int(input("Age:"))
    weight = int(input("Weight:"))
    # if age <= 30 and (weight > w_min and weight < w_max):  # во всех этих сравнениях меня не покидает ощущение что можно было сделать красивее.
    if age <= 30 and (w_min < weight < w_max):
        print('Result:', name, sname, ' | Age:', age, 'Weight:', weight, ' | Good condition!')
        break
    if (age > 30 and age <= 40) and (weight < w_min or weight > w_max):
        print('Result:', name, sname, ' | Age:', age, 'Weight:', weight, ' | Go in for fitness!')
        break
    if age > 40 and (weight < w_min or weight > w_max):
        print('Result:', name, sname, ' | Age:', age, 'Weight:', weight, ' | The patient needs a medical examination!')
        break
    else:
        print('Result:', name, sname, ' | Age:', age, 'Weight:', weight, ' | Cant calculate :(')
        break
