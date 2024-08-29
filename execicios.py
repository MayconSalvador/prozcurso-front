import random

def jogoteste():
    vitorias = 0
    derrotas = 0
    
    while True:
        numero_secreto = random.randint(0, 100)
        
        print("\nNovo jogo de adivinhação do Maycon!")
        print("Tente adivinhar o número entre 0 e 100.")
        print("Você tem 5 tentativas para acertar o número, Boa Sorte!!!")

        tentativas = 0
        max_tentativas = 5

        while tentativas < max_tentativas:
            try:
                palpite = int(input("Digite seu palpite: "))

                if palpite < 0 or palpite > 100:
                    print("Por favor, insira um número entre 0 e 100.")
                    continue

                tentativas += 1

                if palpite == numero_secreto:
                    print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!")
                    vitorias += 1
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
            print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
            derrotas += 1

        print(f"\nPlacar: {vitorias} vitória(s), {derrotas} derrota(s)")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

jogoteste()