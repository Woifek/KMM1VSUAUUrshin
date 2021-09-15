import random
x = random.randint(0,50)
while x != '42':
    x = input('Введите число: ')
    print(int(x)**42)
else:
    print('ОШИБКА: Вы ввели 42')
