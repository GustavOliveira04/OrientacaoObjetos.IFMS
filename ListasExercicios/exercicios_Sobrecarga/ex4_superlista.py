class SuperLista:
    def __init__(self):
        self.__lista = []

    def __gt__(self, valor):
        self.__lista.append(valor)
        return True  

    def __repr__(self):
        if not self.__lista:
            return "Lista vazia"
        else:
            return "\n".join([f"[{i}] = {self.__lista[i]}" for i in range(len(self.__lista))])

# ===================================================================
# Testes

lis = SuperLista()

print(lis)

lis > 10
lis > "Adoro programar"
lis > 42

print(lis)
