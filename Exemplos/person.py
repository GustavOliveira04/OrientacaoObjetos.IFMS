class Person:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    @classmethod
    def fromYear(cls, nome:str, ano:int):
        return cls(nome = nome, idade = 2024 - ano)
    
    @staticmethod
    def isAdult(idade:int):
        return idade > 18

    def __str__(self):
        return f"Person({self.nome}, {self.idade} anos)"
        #cls           ^

#Exemplo de uso 
p1 = Person('Ciclano', idade = 21)
p2 = Person.fromYear(nome = 'Fulano', ano = 2001)
p3 = Person.fromYear(nome = 'Beltrano', ano = 2018)

print(p1)
print(p2)
print(Person.isAdult(p2.idade))
print(Person.isAdult(p3.idade))
