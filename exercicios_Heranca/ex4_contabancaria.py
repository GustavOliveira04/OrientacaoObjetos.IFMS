class ContaBancaria:
    def __init__(self, nome:str, saldo:float):
        self._nome = nome
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser positivo.")
        elif valor > self._saldo:
            print("Saldo insuficiente para o saque.")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")


class ContaCorrente(ContaBancaria):
    def __init__(self, nome:str, saldo:float, limite_cheque_especial:float):
        super().__init__(nome, saldo)
        self._limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser positivo.")
        elif valor > (self._saldo + self._limite_cheque_especial):
            print("Saldo insuficiente, incluindo o cheque especial.")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        saldo_total = self._saldo + self._limite_cheque_especial
        print(f"Saldo atual: R$ {self._saldo:.2f} (incluindo cheque especial: R$ {self._limite_cheque_especial:.2f})")


class ContaPoupanca(ContaBancaria):
    def __init__(self, nome:str, saldo:float, taxa_juros:float):
        super().__init__(nome, saldo)
        self._taxa_juros = taxa_juros

    def aplicar_juros(self):
        juros = self._saldo * self._taxa_juros
        self._saldo += juros
        print(f"Juros de R$ {juros:.2f} aplicados ao saldo.")

# ===================================================================
# Testes

conta_corrente = ContaCorrente("Carlos Miguel", 1559.91, 300.0)
conta_corrente.exibir_saldo()
conta_corrente.sacar(1275)
conta_corrente.exibir_saldo()

print()

conta_poupanca = ContaPoupanca("Claudio Silva", 1774.73, 0.05)
conta_poupanca.exibir_saldo()
conta_poupanca.aplicar_juros()
conta_poupanca.exibir_saldo()