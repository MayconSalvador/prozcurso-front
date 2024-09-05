import unicodedata

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acento = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sem_acento

def quiz_game():
    perguntas = {
        "Qual é a capital da França? ": ("Paris", 10),
        "Quanto é 5 + 7? ": ("12", 5),
        "Quem pintou a Mona Lisa? ": ("Leonardo da Vinci", 15),
        "Qual é o planeta mais próximo do sol? ": ("Mercúrio", 8),
        "Qual é a Distância da Terra e da Lua? ": ("384 mil km", 12),
        "Qual a função do coração? ": ("bombear o sangue", 10)
    }

    print("Bem-vindo ao jogo de perguntas e respostas!\n")

    respostas_jogador = {}
    pontuacao_total = 0

    for pergunta, (resposta_correta, pontuacao) in perguntas.items():
        while True:
            print(f"Pergunta: {pergunta}")
            resposta_jogador_input = input("Sua resposta (ou digite 'mudar' para alterar uma resposta anterior): ")

            if resposta_jogador_input.lower() == 'mudar':
                print("Não é possível mudar a resposta nesta fase. Continue respondendo as perguntas.")
                continue

            resposta_normalizada = remover_acentos(resposta_jogador_input.strip().lower())
            resposta_correta_normalizada = remover_acentos(resposta_correta.strip().lower())

            if resposta_normalizada == resposta_correta_normalizada:
                print(f"Correto! Você ganhou {pontuacao} pontos.\n")
                respostas_jogador[pergunta] = (resposta_jogador_input, pontuacao)
                pontuacao_total += pontuacao
                break
            else:
                print(f"Incorreto! A resposta correta é {resposta_correta}.\n")

    print(f"Você acertou {len(respostas_jogador)} perguntas e obteve {pontuacao_total} pontos no total.")

if __name__ == "__main__":
    quiz_game()