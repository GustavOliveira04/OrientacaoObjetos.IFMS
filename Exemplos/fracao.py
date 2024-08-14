class Fracao():
    def __init__(self, num:int, den:int):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num
    
    @property
    def den(self):
        return self.__den
    
    def __mul__(self, outro:'Fracao'):
        return Fracao(
            num = self.num * outro.num, 
            den = self.den * outro.den
            )
    
    def __str__(self):
        return f"{self.num} / {self.den}"

f1 = Fracao(2, 3)
f2 = Fracao(1, 2)
resultado = f1 * f2
print(resultado)