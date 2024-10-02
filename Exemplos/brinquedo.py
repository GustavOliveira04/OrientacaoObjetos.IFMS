#exemplo

# class Brinquedo:
#     def mover(self):
#         print("Brinquedo movendo...")

# class Aviao(Brinquedo):
#     def mover(self):
#         print("Avião está voando...")

# class Barco(Brinquedo):
#     def mover(self):
#         print("Barco está navegando...")

# class Carro(Brinquedo):
#     def mover(self):
#         print("Carrp está andando...")


#Exercício
class Brinquedo:
    def __init__(self, velocidade:float, aceleracao:float):
        self.velocidade = velocidade
        self.aceleracao = aceleracao

    def mover(self, velocidade:float = 0, aceleracao:float = 0):
        print(f"O brinquedo se moveu com velocidade {velocidade} e {aceleracao} de aceleração")
        
class Carro(Brinquedo):
    #NAO PRECISO DO init se nao for mudar nenhum paramentro!
    def __init__(self, velocidade:float, aceleracao:float):
        super().__init__(velocidade, aceleracao)

    def mover(self, velocidade:float = 0, aceleracao:float = 0):
        print(f"O carro andou com velocidade {velocidade} e {aceleracao} de aceleração ")

class Aviao(Brinquedo):
    #NAO PRECISO DO init se nao for mudar nenhum paramentro!
    def __init__(self, velocidade:float, aceleracao:float):
        super().__init__(velocidade, aceleracao)

    def mover(self, velocidade:float = 0, aceleracao:float = 0):
        print(f"O aviao voou com velocidade {velocidade} e {aceleracao} de aceleração ")

class Barco(Brinquedo):
    #NAO PRECISO DO init se nao for mudar nenhum paramentro!
    def __init__(self, velocidade:float, aceleracao:float):
        super().__init__(velocidade, aceleracao)

    def mover(self, velocidade:float = 0, aceleracao:float = 0):
        print(f"O barco navegou com velocidade {velocidade} e {aceleracao} de aceleração ")
        

c = Carro(velocidade=10, aceleracao=20)
c.mover(110, 10)

a = Aviao(velocidade=156, aceleracao=52)
a.mover(434, 75)

b = Barco(velocidade=65, aceleracao=15)
b.mover(98, 11)


