class FormaGeometrica:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    def calcular_area(self):
        pass

    def calcular_perimentro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        return self.perimetro
    
class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        semi_perimetro = self.calcular_perimetro() / 2
        self.area = (semi_perimetro * 
                     (semi_perimetro - self.lado1) * 
                     (semi_perimetro - self.lado2) * 
                     (semi_perimetro - self.lado3)) ** 0.5
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3
        return self.perimetro
    
# ===================================================================
# Testes

retangulo = Retangulo(10, 15)
print("A Área do retângulo é: ", retangulo.calcular_area())
print("E o seu perimetro é de: ", retangulo.calcular_perimetro())

triangulo = Triangulo(3, 4, 5)
print("\nA Área do triângulo é: ", triangulo.calcular_area())
print("E o perimetro do triangulo é de: ", triangulo.calcular_perimetro())

print("\nO retângulo é uma instância de FormaGeometrica?", isinstance(retangulo, FormaGeometrica))
print("E o triângulo é uma instância de FormaGeometrica?", isinstance(triangulo, FormaGeometrica))
