class MinhaClasse:
    def __init__(self, x:int, y:int):
        self.a = x
        self.b = y

#Exemplo de uso
o1 = MinhaClasse(x = 10, y = 20)
o1.c = 30
print(o1.__dict__)