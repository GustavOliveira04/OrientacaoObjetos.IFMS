from abc import ABC, abstractmethod

class Veiculo(ABC):        # classe é abstrata
    def __init__(self, velocidade:int = 0, marca:str = ''):
        self.velocidade = velocidade
        self.marca = marca

    @abstractmethod
    def mover(self, metros:int):   # método é abstrato
        pass     # não tem corpo

class Carro(Veiculo):
    def __init__(self, velocidade:int = 0, marca:str = '', numPortas:int = 0):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas

    def mover(self, metros:int):
        print(f"O carro moveu {metros} metros")

class Aviao(Veiculo):
    def __init__(self, velocidade:int = 0, marca:str = '', numPortas:int = 0):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas

    def mover(self, metros:int):
        print(f"O Aviao voou {metros} metros")

class Barco(Veiculo):
    def __init__(self, velocidade:int = 0, marca:str = '', numPortas:int = 0):
        super().__init__(velocidade, marca)
        self.numPortas = numPortas

    def mover(self, metros:int):
        print(f"O Barco navegou {metros} metros")
    
c1 = Carro(marca='Honda', velocidade=100, numPortas=4)
a1 = Aviao(marca='Airbuss', velocidade=140, numPortas=2)
b1 = Barco(marca='Mitsubishi', velocidade=75, numPortas=1)

c1.mover(300)
a1.mover(3000)
b1.mover(300)
