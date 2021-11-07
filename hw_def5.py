#Объявлять переменные в аргументах функции это плохо или норма?
def armean(k, s=0, j=0):
    for i in k:
        s = s + int(i)
        j = j + 1
    return s/j
