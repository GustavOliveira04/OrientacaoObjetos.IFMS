# Exercício 4: Faça um programa que possua uma classe chamada BombaCombustivel, com os atributos: • valorLitro • quantidadeCombustivel.

#CORREÇÃO

class BombaCombustivel: 
    def __init__(self,
                 valorlitro:float,
                 quantidadeCombustivel:float ):
        self.__valorlitro = valorlitro
        self.quantidadeCombustivel = quantidadeCombustivel 

    @property
    def valorlitro(self):   #getter
        return self.__valorlitro
    
    @property
    def quantidadeCombustivel(self):    #getter    
        return self.__quantidadeCombustivel


    def abastecerPorValor(self, valor:float):
        litros = valor / self.__valorlitro
        if self.__quantidadeCombustivel >= litros:
            self.__quantidadeCombustivel -= litros
            print(f"Abasteceu: {litros} L")
            print(f"Custo: R$ {valor}")
            return litros
        else: 
            print("Não há combustível suficiente!!")

            
    def abastecerPorLitro(self, litros:float):
        valor = litros * self.__valorlitro
        if self.__quantidadeCombustivel >= litros:
            self.__quantidadeCombustivel -= litros
            print(f"Abasteceu: {litros} L")
            print(f"Custo: R$ {valor} ")
            return valor
        else:
            print("Não há combustível suficiente!!")

    def abastecerPorValor(self, valor:float):
        litros = valor / self.__valorlitro
        self.alterarQuantidadeCombustivel(litros)

    def abastecerPorLitro(self, litros:float):
        self.alterarQuantidadeCombustivel(litros)

    def alterarValor(self, novo_valor:float):  #setter
        if novo_valor > 0:
            self.__valorlitro = novo_valor
        


    #método que retorna verdadeiro caso tenha conseguido abastecer ou falso, caso contrário!!
    def alterarQuantidadeCombustivel(self, litros:float): #-> bool
        valor = litros * self.__valorlitro
        if self.__quantidadeCombustivel >= litros:
            self.__quantidadeCombustivel -= litros
            print(f"Abasteceu: {litros:.2f} L")
            print(f"Custo: R$ {valor:.2f}")
            return True
        else: 
            print("Não há combustível suficiente!!")
            return False

    def __str__(self):# --> str:
        return "\nRelatório da bomba:\n" + \
            f"Valor do Litro: {self.__valorlitro:.2f}\n" + \
            f"Quantidade de combustível: {self.__quantidadeCombustivel:.2f}\n" + \
            "\n"
#------------------------------------------------------------------
b1 = BombaCombustivel(
    valorlitro=5.48,
    quantidadeCombustivel=121.9)

print(b1)
b1.abastecerPorValor(50.00)
print(b1)
b1.abastecerPorLitro(20)
print(b1)
# b1.abastecerPorLitro(93)  #não é possível, pois a quantidade de litros na bomba é menor doq o desejado!
# print(b1)
