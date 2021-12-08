class Date:
    def __init__(self, y = 0, m = 0, d = 0):
        self.y = y
        self.m = m
        self.d = d
    def inputdate (self):
        self.y = int(input("Введите год: "))
        t = int(input("Введите месяц: "))
        if 0 <= t <=12:
            self.m = t
        else:
            print("ОШИБКА: Введен неверный номер месяца!")
            return 0
        t = int(input("Введите день: "))
        if 0 <= t <=31:
            self.d = t
        else:
            print("ОШИБКА: Введен неверный день!")
            return 0
    def printdate (self):
        print("Дата: {0:04d}.{1:02d}.{2:02d}".format(self.y,self.m,self.d))

ndate = Date()
ndate.inputdate()
ndate.printdate()