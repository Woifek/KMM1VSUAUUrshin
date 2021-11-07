#В условии сказано про 1 слово, если несколько то просто загонять их все в список
def pastnum(t=input('Введите текст: ')+' '):
    s = ''
    maxs = ''
    k = []
    kf = []
    f = 0
    for i in t:
        if i.strip():
            s = s + i
        else:
            k.append(s)
            if len(maxs) < len(s):
                maxs = s
            s = ''
    for i in k:
        if k.count(i) > f:
            f = k.count(i)
            kf.clear()
            kf.append(i)
    print('Самое длинное слово: ', maxs, '\nСамое часто встречающееся: ', kf[0])
pastnum()