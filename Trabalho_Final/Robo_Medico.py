from robo import Robo
import random

class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._poder_de_cura = random.uniform(0, 1)

    @property
    def poder_de_cura(self):
        return self._poder_de_cura

    @poder_de_cura.setter
    def poder_de_cura(self, novo_poder_de_cura):
        if 0 <= novo_poder_de_cura <= 1:
            self._poder_de_cura = novo_poder_de_cura
        else:
            raise ValueError("O poder de cura deve estar entre 0 e 1.")

    def criar_bebe(self, nome_filho: str, outro_robo):
        return RoboMedico(nome_filho)

    def curar(self, robo):
        if robo.vida < 1 and self.vida >= robo.vida:
            cura = min(1 - robo.vida, self._poder_de_cura)
            cura = round(cura, 2)
            robo.vida += cura
            print(f'{self.nome} curou {robo.nome} em {cura} pontos de vida!')
        else:
            print(f'{self.nome} não pode curar {robo.nome}!')
