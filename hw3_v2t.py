class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        self.h = h
        self.m = m
        self.s = s
    def inputtime (self):
        t = int(input("Введите часы: "))
        if 0 <= t <=24:
            self.h = t
        else:
            print("ОШИБКА: Введено неверное время!")
            return 0
        t = int(input("Введите минуты: "))
        if 0 <= t <=60:
            self.m = t
        else:
            print("ОШИБКА: Введено неверное время!")
        t = int(input("Введите секунды: "))
        if 0 <= t <=60:
            self.s = t
        else:
            print("ОШИБКА: Введено неверное время!")
    def printtime (self):
        print("Время {0:02d}:{1:02d}:{2:02d}".format(self.h,self.m,self.s))

time = Time()
time.inputtime()
time.printtime()