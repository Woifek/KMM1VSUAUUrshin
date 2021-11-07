def wrlist_ (k = []):
    a = input('Введите что-нибудь:')
    while a.strip():
        k.append(a)
        a = input('Введите что-нибудь:')
    return k
#print(wrlist_())