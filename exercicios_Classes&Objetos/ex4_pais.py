# Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome (ex.: Brasil), população (ex.: 193.946.886) e a sua dimensão em Km2 (ex.: 8.515.767,049). Além 
# disso, cada país mantém uma lista de outros países com os quais ele faz 
# fronteira. Escreva a classe em Python e forneça os seus membros a seguir:
# a) Construtor que inicialize o código ISO, o nome e a dimensão do país; 
# b) Métodos de acesso (getter/setter) para as propriedades código ISO, 
# nome, população e dimensão do país;
# c) Um método que permita verificar se dois objetos representam o 
# mesmo país (igualdade semântica). Dois países são iguais se tiverem 
# o mesmo código ISO;
# d) Um método que informe se outro país é limítrofe do país que recebeu a mensagem;
# e) Um método que retorna a densidade populacional do país;
# f) Um método que receba um país como parâmetro e retorne a lista de 
# vizinhos comuns aos dois países.
# g) Escreva código de teste que instancie objetos de exemplo e demonstre as capacidades da classe

class Pais:
    def __init__(self, codigo:str, nome:str, populacao:int, dimensao:float, fronteiras:list[str]):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__fronteiras = fronteiras

    @property         #getter
    def codigo(self):
        return self.__codigo
    
    @codigo.setter           #setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property         #getter
    def nome(self):
        return self.__nome
    
    @nome.setter           #setter
    def nome(self, nome):
        self.__nome = nome

    @property         #getter
    def populacao(self):
        return self.__populacao
    
    @populacao.setter           #setter
    def populacao(self, populacao):
        self.__populacao = populacao 

    @property         #getter
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter           #setter
    def dimensao(self, dimensao):
        self.__dimensao = dimensao

    @property         #getter
    def fronteiras(self):
        return self.__fronteiras
    
    @fronteiras.setter           #setter
    def fronteiras(self, fronteiras):
        self.__fronteiras = fronteiras

    def comparar (self, pais):
        return pais.codigo == self.codigo
    
    def limitrofe (self, pais):
        return pais.codigo in self.fronteiras
    
    def densi_populacional (self):
        return self.populacao / self.pais
    
    def vizinhos_comuns (self, pais):
        vizinhos_comuns_encontrados = []
        for vizinho in self.fronteiras:
            if vizinho in pais.fronteiras:
                vizinhos_comuns_encontrados.append(vizinho)
        return vizinhos_comuns_encontrados

    
#codigo teste----------------------------------------------
def verificar():
    pais1 = Pais(codigo="BRA", nome="Brasil", populacao=200000000, dimensao=8510000.5, fronteiras=["ARG", "URU", "BOL", ])
    pais2 = Pais(codigo="ARG", nome="Argentina", populacao=4600000, dimensao=2780000.5, fronteiras=["BRA", "URU", "BOL", ])

    vizinhos_comuns = pais1.vizinhos_comuns(pais2)
    print(vizinhos_comuns)
    
verificar ()

