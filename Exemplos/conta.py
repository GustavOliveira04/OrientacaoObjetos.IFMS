class Conta:
    _total_contas = 0

    def __init__(self):
        Conta._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    

#Exemplo de uso
c1 = Conta()
c2 = Conta()
c3 = Conta()
cont = (Conta.get_total_contas())
print(cont)