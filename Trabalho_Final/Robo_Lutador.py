from robo import Robo
import random

class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str):
        super().__init__(nome)
        self._poder = random.uniform(RoboLutador.dano_maximo, 1)

    @property
    def poder(self):
        return self._poder

    @poder.setter
    def poder(self, novo_poder):
        if RoboLutador.dano_maximo <= novo_poder <= 1:
            self._poder = novo_poder
        else:
            raise ValueError(f'O poder deve estar entre {RoboLutador.dano_maximo} e 1.')

    def criar_bebe(self, nome_filho: str, outro_robo):
        return RoboLutador(nome_filho)

    def atacar(self, robo_adversario):
        dano = 1 - self._poder
        robo_adversario.vida *= dano
        dano = round(dano, 2)
        print(f'{self.nome} atacou {robo_adversario.nome} e causou {dano} de dano!')

        if isinstance(robo_adversario, RoboLutador):
            self.full_counter(robo_adversario)

    def full_counter(self, robo_adversario):
        dano = 1 - robo_adversario.poder
        self.vida *= dano
        dano = round(dano, 2)
        print(f'{self.nome} sofreu {dano} de dano de contra-ataque!')

        
