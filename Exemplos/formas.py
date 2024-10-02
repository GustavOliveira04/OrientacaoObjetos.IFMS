import math

class FormaGeometrica:
    def desenha():
        print("Não sei desenha FormaGeometrica")

    def calcula_area():
        print("Não é possível calcular a área de FormaGeometrica")

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado        #atributo de instância

    def desenha(self):
        for y in range(self.lado):
            for x in range(self.lado):
                print('*', end='')
            print()
        

    def calcula_area(self):
        return self.lado * self.lado
        

class Circulo(FormaGeometrica):
    pi = 3.14159                #atributo de classe

    def __int__(self, raio):
        self.raio = raio        #atributo de instância

    def desenha(self):
        pass
    
    def calcula_area(self):
        return Circulo.pi * self.raio ** 2
    

f = FormaGeometrica()
q1 = Quadrado(lado = 4)
q2 = Quadrado(lado = 8)
c1 = Circulo(raio = 5)
c2 = Circulo(raio = 10)

q1.desenha()
