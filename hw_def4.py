#Как я понял для вывода как в задании нужно использовать матрицу?
#или это просто пример вывода?
import hw_def1

def func_v1(k: list):
    k.sort()
    while k != []:
        n = k.count(k[0])
        s = [k[0], n]
        print(s)
        for j in range(n):
            k.remove(k[0])

def func_v2(k: list):
    k.sort()
    print('Элемент | Частота')
    while k != []:
        n = k.count(k[0])
        print(k[0], ' | ', n)
        for j in range(n):
            k.remove(k[0])
#func_v1(hw_def1.wrlist_())