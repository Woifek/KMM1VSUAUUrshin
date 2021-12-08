class Fract:
    def __init__ (self, num = 0, denom = 0):
        self.num = num
        self.denom = denom
    def inputfract (self):
        self.num = input("Введите числитель: ")
        self.denom = input("Введите знаменатель: ")
    def printfract (self):
        print(self.num,"/",self.denom)

fract = Fract()
fract.inputfract()
fract.printfract()