k = []
for b in range(2):
    for d in range(3):
        x = input('Введите '+str(d+1)+'ю координату для вектора №' + str(b+1)+': ')
        k.append(x)
for b in range(3):
    k.append(k[b]+k[b+3])
print(k[7],k[8],k[9])