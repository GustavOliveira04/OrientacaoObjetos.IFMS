# screva em Python uma classe Ponto2D que represente um ponto no plano
# cartesiano. A classe deve ter os parâmetros que representam abcissa e ordenada, isto é, o valor de X e Y do ponto. A classe também deve oferecer os 
# seguintes membros:
# a) Construtor que permita a inicialização do ponto:
# • Por default (sem parâmetros) na origem do espaço 2D
# • Num local indicado por dois parâmetros do tipo float (indicando o valor de abcissa e ordenada do ponto que está sendo 
# criado);
# b) Métodos de acesso (getter/setter) dos atributos do ponto
# c) Método denominado compara, que recebe um Ponto2D como parâmetro e retorna verdadeiro caso sejam o mesmo ponto, ou falso, 
# caso contrário
# d) Método de representação do objeto como string
# e) Método que permita calcular a distância do ponto do objeto, para outro ponto recebido como parâmetro
# f) Método clone, que retorna uma nova instância de um ponto no 
# mesmo local do objeto.
# g) Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe.

import math
class Ponto2D:
# A)  #-contrutor
    def __init__(self, x = 0.0, y = 0.0):  
        self.__x = x
        self.__y = y

# B)  # métodos de X
    @property           #getter  
    def x(self):
        return self.__x
    
    @x.setter           #setter
    def x(self, x):
        self.__x = x

#       métodos de Y
    @property           #getter  
    def y(self):
        return self.__y
    
    @y.setter           #setter
    def y(self, y):
        self.__y = y

# C) Método compara
    def compara(self, outro_ponto):
        if (self.__x == outro_ponto.x and self.__y == outro_ponto.y):
            return True #1
        else:
            return False #0  

# D) Representando como string        
    def __str__(self):
        return f'\nx:({self.__x}) \ny:({self.__y})\n'

# E) calcular a distância do ponto, para outro ponto recebido como parâmetro
    def dist(x2, y2, x1, y1):
        a = (x2 - x1)**2 + (y2 - y1)**2
        b = math.sqrt(a)
        return b

# F) Método clone, que retorna uma nova instância
    def clone(self):
        return Ponto2D(self.__x, self.__y)

# G) Código Teste -------------------------------------------------------
def teste():
    p1 = Ponto2D()
    p2 = Ponto2D(3.8, 4.0)

    print(f"p1:{p1}")
    print(f"p2:{p2}")

    p1.x = 1.5
    p1.y = 2.4
    print(f"p1 Atualizado: {p1}\n")

    p2.x = 4.5
    p2.y = 1.4
    print(f"p2 Atualizado: {p2}\n")

teste()