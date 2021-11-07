def pastnum(n):
    if n > 1:
        if n == 2 or n == 3:
            return True
        elif n % 2 == 0:
            return False
        for i in range(3, n+1):
            if n % i == 0:
                return True
            i = i + 2
    return False
print(pastnum(int(input('Введите: '))))