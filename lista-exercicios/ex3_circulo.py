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
    def __init__(self, raio:float, ponto:Ponto2D):
        self.__raio = raio
        self.__ponto = ponto

    @property       #getter
    def raio(self):
        return self.__raio
    
    @raio.setter    #setter
    def raio(self):
        return self.__raio

    def inflar(self, value):
        self.__raio += value

    def desinflar(self, value):
        if value >= self.__raio: 
            print("Erro!")
            return
        
        self.__raio -= value

    def mover(self, novo_ponto):
        if novo_ponto:
            self.__ponto = novo_ponto
            return

        self.__ponto = Ponto2D()

    def area(self):
        return self.__raio**2 * pi
    

#codigo teste-------------------------------------------
def teste_get_set():
    circulo = Circulo(10, Ponto2D)

    circulo.__raio = 25
    return circulo.__raio == 25

def testes():
    teste_get_set()


testes()
        


