class Funcionario:
    def __init__(self, nome, cpf, salario, departamento):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento

    def bonificar(self):
        self.salario *= 1.10

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento, senha, numero_funcionarios_gerenciados):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        self.numero_funcionarios_gerenciados = numero_funcionarios_gerenciados

    def autenticar_senha(self, senha):
        return self.senha == senha
    
    def bonificar(self):
        self.salario *= 1.15

# ===================================================================
# Testes

funcionario = Funcionario("Claudio","412.643.135-64", 2500, "TI")
print(f'O salário do funcionario antes da bonificação era de: R$ {funcionario.salario}')

funcionario.bonificar()
print(f'O salário do funcionario depois da bonificação é de: R$ {funcionario.salario}')


gerente = Gerente("Rodrigo", "532.162.765-53", 5000, "TI", "987654321sEnHa", 7)
print(f'O salário do gerente antes da bonificação é de: R$ {gerente.salario}')

gerente.bonificar()
print(f'O salário do gerente depois da bonificação é de: R$ {gerente.salario}')


senha = "987654321sEnHa"
print(f'Autenticação com a senha {senha}:', gerente.autenticar_senha(senha))

senha_errada = '12312344112'
print(f'Autenticação com a senha {senha_errada}:', gerente.autenticar_senha(senha_errada))