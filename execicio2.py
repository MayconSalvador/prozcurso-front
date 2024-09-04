def quiz_game():
    perguntas = {
        "Qual é a capital da França? ": "Paris",
        "Quanto é 5 + 7? ": "12",
        "Quem pintou a Mona Lisa? ": "Leonardo da Vinci",
        "Qual é o planeta mais próximo do sol? ": "Mercúrio",
    }

    print("Bem-vindo ao jogo de perguntas e respostas!\n")

    placar = 0
    total_perguntas = len(perguntas)


    for pergunta, resposta_correta in perguntas.items():
 
        resposta_jogador = input(pergunta)

        if resposta_jogador.strip().lower() == resposta_correta.lower():
            print("Correto!\n")
            placar += 1
        else:
            print(f"Incorreto! A resposta correta é {resposta_correta}.\n")

    print(f"Você acertou {placar} de {total_perguntas} perguntas.")

if __name__ == "__main__":
    quiz_game()