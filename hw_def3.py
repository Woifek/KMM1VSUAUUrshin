def fibch(n, k=[0], j=0, i=0):
    if int(n) == 1:
        return k
    elif int(n) >= 2:
        k.append(1)
    for i in range(int(n)-2):
        j = k[i] + k[i+1]
        k.append(j)
    return k
#print(fibch(input('Введите число: ')))