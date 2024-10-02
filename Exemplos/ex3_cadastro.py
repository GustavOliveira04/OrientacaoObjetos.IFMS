# Excercício 3: Implemente a classe Cadastro que representa um perfil de usuário com atributos login e senha. O login deve ter entre 5 e 15 caracteres, e a senha
# deve ter no mínimo 8 caracteres. Ambos os atributos devem ser privados e a classe deve implementar getters e setters através de propriedades

class Cadastro:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

# métodos ------------------------
    @property
    def login (self):
        return self.__login
    
    @property
    def senha (self):
        return self.__senha 
    
    @login.setter
    def login (self, login):
       if len(login) >= 5 and len (login) <= 15:
            self.__login = login
       else:
           print("Login Inválido!!")

    @senha.setter
    def senha (self, senha):
       if len(senha) >= 8: 
            self.__senha = senha
       else:
            print("Senha inválida!!")


#---------------------------------
logar = Cadastro('João Bobão', '123456789')
print('Login:', logar.login,"  ",'Senha:', logar.senha)

logar.login = 'Novo Login'
logar.senha = 'Nova Senha' 

# logar.login = 'ABC' # não funciona
# logar.senha = '123' # não funciona


print('Login:', logar.login,"  ",'Senha:', logar.senha)
