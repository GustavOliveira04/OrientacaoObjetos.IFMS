import random
from Robo_Lutador import RoboLutador
from Robo_Medico import RoboMedico

def batalha_dinamica(robo1, robo2, robo_medico):
    rodada = 1
    max_rodadas = 7

    while robo1.vida > 0 and robo2.vida > 0 and rodada <= max_rodadas:
        print(f"\n--- Rodada {rodada} ---")
        
        print(f"\n{robo1.nome} ataca {robo2.nome}")
        robo1.atacar(robo2)

        if robo2.precisa_de_medico():
            chamar_robo_medico(robo2, robo_medico)

        if robo2.vida > 0:
            print(f"\n{robo2.nome} ataca {robo1.nome}")
            robo2.atacar(robo1)

            if robo1.precisa_de_medico():
                chamar_robo_medico(robo1, robo_medico)
        
        print(f"\nSituação dos robôs após a rodada {rodada}:")
        print(f"{robo1.nome}: {robo1.vida} de vida")
        print(f"{robo2.nome}: {robo2.vida} de vida")
        
        rodada += 1

    if robo1.vida <= 0:
        print(f"\n{robo2.nome} venceu a batalha!")
    elif robo2.vida <= 0:
        print(f"\n{robo1.nome} venceu a batalha!")
    else:
        print(f"\nA batalha terminou em empate após {max_rodadas} rodadas!")

def chamar_robo_medico(robo, robo_medico):

    chance_de_atendimento = random.random()
    if chance_de_atendimento <= 0.5:
        print(f"\n{robo_medico.nome} foi chamado para curar {robo.nome}.")
        robo_medico.curar(robo)
    else:
        print(f"\n{robo_medico.nome} foi chamado, mas decidiu não curar {robo.nome}.")

if __name__ == "__main__":

    lutador1 = RoboLutador("NoisyBoy")
    lutador2 = RoboLutador("Zeus")

    medico = RoboMedico("Reparador")

    print(f"\nStatus inicial dos robôs:")
    print(f"{lutador1.nome}: {lutador1.vida} de vida")
    print(f"{lutador2.nome}: {lutador2.vida} de vida")
    print(f"{medico.nome}: {medico.vida} de vida")

    batalha_dinamica(lutador1, lutador2, medico)


