from abc import ABC, abstractmethod

class Empregado(ABC):   # classe é abstrata
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def ganha(self):    # método é abstrato
        pass  # não tem corpo

class Horista(Empregado):
    def ganha(self):
        print("Ganhou salário")

h1 = Horista(nome='Fulano', idade=30)
h1.ganha()
