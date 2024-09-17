class Ponto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Ponto):
            return Ponto(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("A adição deve ser realizada entre dois objetos do tipo Ponto.")
    
    def __sub__(self, other):
        if isinstance(other, Ponto):
            return Ponto(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("A subtração deve ser realizada entre dois objetos do tipo Ponto.")
    
    def __mul__(self, other):
        if isinstance(other, Ponto):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("A multiplicação deve ser realizada entre dois objetos do tipo Ponto.")
    
    def __rmul__(self, escalar):
        if isinstance(escalar, (int, float)):
            return Ponto(escalar * self.x, escalar * self.y)
        else:
            raise TypeError("O multiplicador deve ser um número (int ou float).")

# ===================================================================
# Testes

p1 = Ponto(4, 5)
p2 = Ponto(2, 3)

print("Ponto 1:", p1)
print("Ponto 2:", p2)

p3 = p1 + p2
print("P1 + P2:", p3)

p4 = p1 - p2
print("P1 - P2:", p4)

produto_escalar = p1 * p2
print("P1 * P2 (Produto escalar):", produto_escalar)

p5 = 2 * p1
print("2 * P1:", p5)
