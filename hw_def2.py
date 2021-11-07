def season_v1 (n):
    wi = ['12','1','2']
    sp = ['3','4','5']
    su = ['6','7','8']
    au = ['9','10','11']
    if wi.count(n):
        return 'Зима'
    elif sp.count(n):
        return 'Весна'
    elif su.count(n):
        return 'Лето'
    elif au.count(n):
        return 'Осень'
    else:
        return 'Нет такого месяца'

def season_v2 (n):
    if int(n) > 12 or n < 1:
        return 'Нет такого месяца'
    k = [['12','1','2'],['3','4','5'],['6','7','8'],['9','10','11']]
    res = [0 for i in k if i[0]==n][0]#Что тут происходит?
    if res == 0:
        return 'Зима'
    elif res == 1:
        return 'Весна'
    elif res == 2:
        return 'Лето'
    elif res == 3:
        return 'Осень'
#n = input('Введите месяц: ')
#print(season_v2(n))