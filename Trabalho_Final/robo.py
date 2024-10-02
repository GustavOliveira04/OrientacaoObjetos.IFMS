import random

class Robo:
    nivel_critico = 0.60

    def __init__(self, nome: str):
        self._nome = nome
        self._vida = random.uniform(0, 1)
        self._vida = round(self._vida, 2)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nova_vida):
        if 0 <= nova_vida <= 1:
            self._vida = round(nova_vida, 2)
        else:
            raise ValueError("A vida deve estar entre 0 e 1.")

    def __repr__(self):
        return f'Nome do robô: {self._nome}, vida do robô: {self._vida}'

    def __add__(self, outro_robo):
        nome_pai = self._nome.split('-')[0]
        nome_mae = outro_robo.nome.split('-')[0]
        nome_filho = f'{nome_pai}-{nome_mae}'
        return self.criar_bebe(nome_filho, outro_robo)

    def criar_bebe(self, nome_filho: str, outro_robo):
        return Robo(nome_filho)

    def precisa_de_medico(self):
        return self._vida < Robo.nivel_critico


