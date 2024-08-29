import random
##JOGO DE SORTEIO
def jogoteste():
    numero_secreto = random.randint(0, 100)

    print("Bem-vindo ao jogo de adivinhação do Maycon!")
    print("Tente adivinhar o número entre 0 e 100 que eu escolhi e direi se esta perto ou nao.")
    print("Você tem 5 tentativas para acertar o número.")

    tentativas = 0
    max_tentativas = 5

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))

            if palpite < 0 | palpite > 100:
                print("Por favor, insira um número entre 0 e 100.")
                continue

            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
                break
            elif palpite < numero_secreto:
                print("O número é maior.")
            else:
                print("O número é menor.")

            if tentativas < max_tentativas:
                print(f"Você tem {max_tentativas - tentativas} tentativa(s) restante(s).")

        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    if tentativas == max_tentativas:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}. Boa sorte na próxima vez!")

jogoteste()