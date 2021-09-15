y = []
x = input('Введите число: ')
while x != '42':
    y.append(x)
    x = input('Введите число: ')
print('ОШИБКА: Вы ввели 42', y)

