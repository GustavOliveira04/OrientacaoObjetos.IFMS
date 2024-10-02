class Inteiro():
    def __init__(self, valor:int):
        self.valor = valor

    def __add__(self, outro):
        return self.valor + outro.valor

i1 = Inteiro(5)
i2 = Inteiro(4)
print(i1 + i2)
