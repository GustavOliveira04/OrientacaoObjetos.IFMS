# Exercício 1: Modifique o código da classe a seguir para transformar getter e setter usando o padrão de propriedade em Python:
# Exercício 2: No código do exercício anterior, modifique o setter de forma que não seja permitido armazenar um valor negativo para a idade
#-------------------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

# métodos ------------------------
    @property   # getter
    def age(self):
        return self.__age
    
    @age.setter   # setter
    def age(self, age):
        if age > 0:
            self.__age = age

#-----------------------
stud = Student('Vanessa', 19)
print('Name:', stud.name, stud.age) # obtém idade usando getter
stud.age = -6 # altera idade usando setter
print('Name:', stud.name, stud.age) # obtém idade usando getter

#PRIMEIRO EXERCÍCIO Q EU FAÇO Q DA BOM. RECEBA!!