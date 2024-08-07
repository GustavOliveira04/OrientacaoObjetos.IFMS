# Escreva em Python uma classe Circulo, que representa um círculo no 
# plano cartesiano. Forneça os seguintes membros de classe:
# a) Um construtor que receba o raio e um ponto (o centro do círculo). O 
# parâmetro ponto deve ser do tipo Ponto2D criado anteriormente.
# b) Métodos de acesso ao atributo raio do círculo
# c) Métodos inflar e desinflar, que, respectivamente, aumentam e diminuem o raio do círculo de um dado valor
# d) Método mover, que recebe um ponto por parâmetro, que:
# • caso o ponto não seja passado, leva o círculo para a origem do
# espaço 2D, isto é, ponto (0, 0)
# • caso o ponto seja passado, move o círculo para o ponto indicado pelo parâmetro
# e) Método que retorna a área do círculo
# Escreva código de teste que instancie objetos de exemplo e demonstre as 
# capacidades da classe.

from ex2_ponto2d import Ponto2D
from math import pi

class Circulo: 
    def __init__(self, raio:float, centro):
        self.__raio = raio
        self.__centro = centro

    @property       #getter
    def raio(self):
        return self.__raio
    
    @raio.setter    #setter
    def raio(self, value):
        self.__raio = value
        

    def inflar(self, value):
        self.__raio += value

    def desinflar(self, value):
        if value >= self.__raio: 
            print("Erro!")
            return
        
        self.__raio -= value

    def mover(self, novo_centro=None):
        if novo_centro is None:
            self.__centro = Ponto2D(0.0 , 0.0)
        else:
            self.__centro = novo_centro
            

    def area(self):
        return self.__raio**2 * pi
    

#codigo teste-------------------------------------------
def teste_get_set():
    centro1 = Ponto2D(1.0, 1.0)
    centro2 = Ponto2D(3.0, 4.0)

    # Criando círculos
    circulo1 = Circulo(5.0, centro1)
    circulo2 = Circulo(10.0, centro2)

    # Testando getters e setters
    print(f"Circulo1: {circulo1}")  # Circulo1: Circulo(raio=5.0, centro=Ponto2D(1.0, 1.0))
    print(f"Circulo2: {circulo2}")  # Circulo2: Circulo(raio=10.0, centro=Ponto2D(3.0, 4.0))

    circulo1.raio = 7.0
    print(f"Novo Circulo1: {circulo1}")  # Novo Circulo1: Circulo(raio=7.0, centro=Ponto2D(1.0, 1.0))

    # Testando inflar e desinflar
    circulo1.inflar(3.0)
    print(f"Circulo1 inflado: {circulo1}")  # Circulo1 inflado: Circulo(raio=10.0, centro=Ponto2D(1.0, 1.0))

    circulo1.desinflar(2.0)
    print(f"Circulo1 desinflado: {circulo1}")  # Circulo1 desinflado: Circulo(raio=8.0, centro=Ponto2D(1.0, 1.0))

    # Testando o método mover
    circulo1.mover()
    print(f"Circulo1 movido para a origem: {circulo1}")   # Circulo1 movido para a origem: Circulo(raio=8.0, centro=Ponto2D(0.0, 0.0))

    circulo1.mover(Ponto2D(2.0, 2.0))
    print(f"Circulo1 movido para (2.0, 2.0): {circulo1}")  # Circulo1 movido para (2.0, 2.0): Circulo(raio=8.0, centro=Ponto2D(2.0, 2.0))

    # Testando a área do círculo
    area_circulo1 = circulo1.area()
    print(f"Área do Circulo1: {area_circulo1}")  # Área do Circulo1: 201.06192982974676


#     circulo = Circulo(10, Ponto2D)

#     circulo.__raio = 25
#     return circulo.__raio == 25

# def testes():
#     teste_get_set()


# testes()
        


