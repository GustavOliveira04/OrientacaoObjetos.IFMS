# class Animal:
#     def mover(self, m:int):
#         print(f"O animal moveu {m} metros.")

# class Gato(Animal):
#     def mover(self, m:int):
#         print(f"O gato andou {m} metros.")

# class Peixe(Animal):
#     def mover(self, m:int):
#         print(f"O peixe nadou {m} metros.")

class Animal:
    def __init__(self, nome:str, tamanho:int):
        self.nome = nome
        self.tamanho = tamanho

    def mover(self, m:int):
        print(f"O animal moveu {m} metros")

class Gato(Animal):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, tamanho)

    def mover(self, m:int):
        print(f"O gato andou {m} metros")

g = Gato(nome = "Mingau", tamanho = 10)
g.mover(10)
