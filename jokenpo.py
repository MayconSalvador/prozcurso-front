import random

def jokenpo():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    contador_jogadas = 0

    while True:
        computador = random.choice(opcoes)
        jogador = input("Escolha Pedra, Papel, Tesoura ou 'Sair' para encerrar: ").capitalize()

        if jogador == 'Sair':
            print(f"Jogo encerrado! Você jogou {contador_jogadas} vez(es).")
            break

        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        contador_jogadas += 1

        print(f"Você escolheu: {jogador}")
        print(f"O computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == 'Pedra' and computador == 'Tesoura') or \
             (jogador == 'Papel' and computador == 'Pedra') or \
             (jogador == 'Tesoura' and computador == 'Papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

# Executa o jogo
jokenpo()