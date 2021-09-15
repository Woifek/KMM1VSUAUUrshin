x = input('Введи x ')
x = int(x) * 2
y = input('Введи y ')
y = int(y) - 2
if x > y:
    print('x>y')
elif y > x:  
    print('y<x')
else:
    print('x=y')