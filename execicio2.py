import unicodedata

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acento = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acento

def quiz_game():
    perguntas = {
        "Qual é a capital da França? ": "Paris",
        "Quanto é 5 + 7? ": "12",
        "Quem pintou a Mona Lisa? ": "Leonardo da Vinci",
        "Qual é o planeta mais próximo do sol? ": "Mercúrio",
        "Qual é a Distância da Terra e da Lua? ": "384 mil km",
        "Qual a função do coração? ": "bombear o sangue"
    }

    print("Bem-vindo ao jogo de perguntas e respostas!\n")

    placar = 0
    total_perguntas = len(perguntas)

    for pergunta, resposta_correta in perguntas.items():
        resposta_jogador = input(pergunta)


        resposta_normalizada = remover_acentos(resposta_jogador.strip().lower())
        resposta_correta_normalizada = remover_acentos(resposta_correta.strip().lower())

        if resposta_normalizada == resposta_correta_normalizada:
            print("Correto!\n")
            placar += 1
        else:
            print(f"Incorreto! A resposta correta é {resposta_correta}.\n")

    print(f"Você acertou {placar} de {total_perguntas} perguntas.")

if __name__ == "__main__":
    quiz_game()