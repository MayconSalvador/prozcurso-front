import random

def jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    contador_jogadas = 0

    while True:
        computador = random.choice(opcoes)
        jogador = input("Escolha Pedra, Papel, Tesoura ou 'Sair' para encerrar: ").strip().lower()

        if jogador == 'sair':
            print(f"Jogo encerrado! Você jogou {contador_jogadas} vez(es).")
            break

        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        contador_jogadas += 1

        print(f"Você escolheu: {jogador.capitalize()}")
        print(f"O computador escolheu: {computador.capitalize()}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

jokenpo()