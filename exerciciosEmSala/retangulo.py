# class Retangulo:
#     #atributos de classe
#     lado1 = 0
#     lado2 = 0

#     def __init__(self, lado1, lado2):
#         self.lado1 = lado1
#         self.lado2 = lado2

#     def area(self):
#         return self.lado1 * self.lado2
    
#     def perimetro(self):
#         return 2 * (self.lado1 + self.lado2)
    
#     def set_lados(cls, novo_lado1, novo_lado2):
#         cls.lado1 = novo_lado1
#         cls.lado2 = novo_lado2


# #Exemplo de uso
# r1 = Retangulo(2, 4)
# r2 = Retangulo(4, 8)

# print("A area de de r1 é:", r1.area())
# print("O perimetro de r1 é:", r1.perimetro())

# print("A area de r2 é:", r2.area())
# print("O perimetro de r2 é:", r2.perimetro())


class Retangulo:
    #atributo de classe
    lado1 = 0
    lado2 = 0

    def area(self):
        return Retangulo.lado1 * Retangulo.lado2
    
    def perimetro(self):
        return 2 * Retangulo.lado1 + 2 * Retangulo.lado2
    
    @classmethod
    def set_lados(cls, novo_lado1:float, novo_lado2:float):
        cls.lado1 = novo_lado1
        cls.lado2 = novo_lado2

    def __str__(self):
        return f"Retando({Retangulo.lado1}, {Retangulo.lado2})"


#Exemplo de uso
r1 = Retangulo()
r2 = Retangulo()
r3 = Retangulo()

Retangulo.set_lados(4, 8)
print(r1.area())
print(r1.perimetro())
