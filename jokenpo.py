import random
import tkinter as tk
from tkinter import messagebox

# Função para determinar o vencedor
def determinar_vencedor(jogador, computador):
    regras = {
        'pedra': ['tesoura', 'lagarto'],
        'papel': ['pedra', 'spock'],
        'tesoura': ['papel', 'lagarto'],
        'lagarto': ['spock', 'papel'],
        'spock': ['tesoura', 'pedra']
    }

    if jogador == computador:
        return "Empate"
    elif computador in regras[jogador]:
        return "Vitória"
    else:
        return "Derrota"

# Função para a escolha do computador
def escolha_computador(dificuldade):
    if dificuldade == 'difícil' and historico:
        ultima_jogada_jogador = historico[-1][0]
        return escolher_contra(ultima_jogada_jogador)
    return random.choice(opcoes)

def escolher_contra(jogada):
    if jogada == 'pedra':
        return 'papel'
    elif jogada == 'papel':
        return 'tesoura'
    elif jogada == 'tesoura':
        return 'pedra'
    elif jogada == 'lagarto':
        return 'tesoura'
    elif jogada == 'spock':
        return 'lagarto'

# Função que é chamada quando um botão é clicado
def jogar(jogador):
    global vitorias, derrotas, empates, historico, contador_jogadas

    computador = escolha_computador(dificuldade.get())
    resultado = determinar_vencedor(jogador, computador)

    contador_jogadas += 1
    historico.append((jogador, computador, resultado))

    if resultado == "Vitória":
        vitorias += 1
    elif resultado == "Derrota":
        derrotas += 1
    else:
        empates += 1

    # Atualiza o histórico e pontuação na interface
    texto_historico.set(f"Você: {jogador.capitalize()} | Computador: {computador.capitalize()} | Resultado: {resultado}")
    pontuacao.set(f"Vitórias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}")

    # Mostrar mensagem de resultado
    messagebox.showinfo("Resultado", f"Você escolheu {jogador.capitalize()}, Computador escolheu {computador.capitalize()}.\n{resultado}!")

# Função para reiniciar o jogo
def reiniciar():
    global vitorias, derrotas, empates, historico, contador_jogadas

    vitorias = 0
    derrotas = 0
    empates = 0
    historico = []
    contador_jogadas = 0

    texto_historico.set("Faça sua escolha!")
    pontuacao.set("Vitórias: 0 | Derrotas: 0 | Empates: 0")

# Cria a janela principal
janela = tk.Tk()
janela.title("Jokenpô")

# Variáveis globais
opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
vitorias = 0
derrotas = 0
empates = 0
historico = []
contador_jogadas = 0

# Configurações da interface
dificuldade = tk.StringVar(value='fácil')
texto_historico = tk.StringVar(value="Faça sua escolha!")
pontuacao = tk.StringVar(value="Vitórias: 0 | Derrotas: 0 | Empates: 0")

# Labels e botões
label_titulo = tk.Label(janela, text="Jokenpô", font=("Arial", 24))
label_titulo.pack(pady=10)

label_dificuldade = tk.Label(janela, text="Escolha a dificuldade:", font=("Arial", 14))
label_dificuldade.pack()

dificuldade_f = tk.Radiobutton(janela, text="Fácil", variable=dificuldade, value='fácil', font=("Arial", 12))
dificuldade_f.pack()

dificuldade_d = tk.Radiobutton(janela, text="Difícil", variable=dificuldade, value='difícil', font=("Arial", 12))
dificuldade_d.pack()

label_historico = tk.Label(janela, textvariable=texto_historico, font=("Arial", 14))
label_historico.pack(pady=10)

label_pontuacao = tk.Label(janela, textvariable=pontuacao, font=("Arial", 14))
label_pontuacao.pack(pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

for opcao in opcoes:
    botao = tk.Button(frame_botoes, text=opcao.capitalize(), width=10, height=2, font=("Arial", 12), command=lambda o=opcao: jogar(o))
    botao.pack(side=tk.LEFT, padx=5)

botao_reiniciar = tk.Button(janela, text="Reiniciar", font=("Arial", 12), command=reiniciar)
botao_reiniciar.pack(pady=10)

# Executa o loop principal da interface
janela.mainloop()