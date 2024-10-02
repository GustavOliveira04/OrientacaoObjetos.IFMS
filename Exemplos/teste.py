class MinhaClasse:
    __slots__ = ['a', 'b', 'c']
    
    def __init__(self, x:int, y:int):
        self.a = x
        self.b = y

#Exemplo de uso
o1 = MinhaClasse(x = 10, y = 20)
o1.c = 30
o1.d = 40
print(dir(o1))
print(o1.__dict__)

