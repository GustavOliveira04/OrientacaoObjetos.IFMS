class Relogio:
    def __init__(self, hora, minuto, segundo):
        if not (0 <= hora < 24):
            print("Hora inválida!")
            self.hora = 0
        else:
            self.hora = hora

        if not (0 <= minuto < 60):
            print("Minuto inválido!")
            self.minuto = 0
        else:
            self.minuto = minuto

        if not (0 <= segundo < 60):
            print("Segundo inválido!")
            self.segundo = 0
        else:
            self.segundo = segundo

    def __repr__(self):
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"

    def __add__(self, other):
        segundos_totais = self.to_segundos() + other.to_segundos()
        return Relogio.from_segundos(segundos_totais)

    def __sub__(self, other):
        if self <= other:
            print("O primeiro horário deve ser maior que o segundo")
            return None
        else:
            segundos_totais = self.to_segundos() - other.to_segundos()
            return Relogio.from_segundos(segundos_totais)

    def __eq__(self, other):
        return self.to_segundos() == other.to_segundos()

    def __gt__(self, other):
        return self.to_segundos() > other.to_segundos()

    def __lt__(self, other):
        return self.to_segundos() < other.to_segundos()

    def __ge__(self, other):
        return self.to_segundos() >= other.to_segundos()

    def __le__(self, other):
        return self.to_segundos() <= other.to_segundos()

    def to_segundos(self):
        return self.hora * 3600 + self.minuto * 60 + self.segundo

    @classmethod
    def from_segundos(cls, segundos_totais):
        segundos_totais %= 86400
        hora = segundos_totais // 3600
        segundos_totais %= 3600
        minuto = segundos_totais // 60
        segundo = segundos_totais % 60
        return cls(hora, minuto, segundo)

# ===================================================================
# Testes

r0 = Relogio(16, 61, 54)
r1 = Relogio(18, 37, 32)
r2 = Relogio(20, 0, 30)

print(r1)
print(r2)

r3 = r1 + r2
print(r3)

r4 = r3 - r2
print(r4)

r4 = r2 - r3
print(r4)

print(r1 == r2)
print(r1 == Relogio(18, 37, 32))
print(r3 > r3)
print(r3 > r2)
print(r2 > r3)
print(r1 < r2)
