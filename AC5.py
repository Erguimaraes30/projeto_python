from random import randint

def main():
# Atributos do aventureiro
    vida_aventureiro = 100
    ataque_aventureiro = randint(10, 20)
    defesa_aventureiro = randint(1, 5)
# Atributos do monstro
    vida_monstro = randint(60, 80)
    ataque_monstro = randint(20, 30)
# Atributos iniciais
    print("Vida do Aventureiro =", vida_aventureiro, "//Ataque do Aventureiro =", ataque_aventureiro, "//Defesa do Aventureiro =", defesa_aventureiro)
    print("Vida do Monstro=", vida_monstro, "//Ataque do Monstro=", ataque_monstro)

    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("\nRodada", rodada)
        rodada = rodada + 1



# Dano Aventureiro
        dano_aventureiro = randint(1, ataque_aventureiro)
        vida_monstro = vida_monstro - dano_aventureiro
# Dano Monstro
        dano_monstro = randint(1, ataque_monstro) - defesa_aventureiro
        vida_aventureiro = vida_aventureiro - dano_monstro

        if vida_aventureiro <= 0:
            print("O Aventureiro Morrreu")
            break
        if vida_monstro <= 0:
            print("O Monstro morreu")
            break

        print("Aventureiro: Vida=", vida_aventureiro, "//Ataque=", ataque_aventureiro, "//Defesa=", defesa_aventureiro)
        print("Monstro: Vida=", vida_monstro, "Ataque=", ataque_monstro)


main()
