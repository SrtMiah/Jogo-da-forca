import random
import tkinter as tk
from tkinter import messagebox

palavras = ['python', 'programacao', 'jogo', 'desenvolvimento', 'computador']

def escolher_palavra():
    return random.choice(palavras)

def exibir_palavra(palavra, letras_certas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_certas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao.strip()

def nova_partida():
    global palavra, letras_certas, letras_erradas, tentativas
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6
    palavra_label.config(text=exibir_palavra(palavra, letras_certas))
    erros_label.config(text=f"Erros: {', '.join(letras_erradas)}")
    tentativas_label.config(text=f"Tentativas restantes: {tentativas}")
    letra_entry.delete(0, tk.END)

def verificar_letra():
    global tentativas
    letra = letra_entry.get().lower()
    letra_entry.delete(0, tk.END)

    if letra in letras_certas or letra in letras_erradas:
        messagebox.showinfo("Letra repetida", "Você já tentou essa letra. Tente outra.")
        return

    if letra in palavra:
        letras_certas.append(letra)
        if set(letras_certas) == set(palavra):
            palavra_label.config(text=palavra)
            messagebox.showinfo("Parabéns!", f"Você adivinhou a palavra: {palavra}")
            nova_partida()
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        if tentativas == 0:
            palavra_label.config(text=palavra)
            messagebox.showinfo("Game over", f"Você perdeu! A palavra era: {palavra}")
            nova_partida()

    palavra_label.config(text=exibir_palavra(palavra, letras_certas))
    erros_label.config(text=f"Erros: {', '.join(letras_erradas)}")
    tentativas_label.config(text=f"Tentativas restantes: {tentativas}")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Jogo da Forca")

palavra_label = tk.Label(janela, text="", font=("Helvetica", 20))
palavra_label.pack(pady=20)

letra_entry = tk.Entry(janela, font=("Helvetica", 20))
letra_entry.pack(pady=10)

verificar_button = tk.Button(janela, text="Verificar Letra", command=verificar_letra, font=("Helvetica", 20))
verificar_button.pack(pady=10)

erros_label = tk.Label(janela, text="Erros: ", font=("Helvetica", 14))
erros_label.pack(pady=10)

tentativas_label = tk.Label(janela, text="Tentativas restantes: ", font=("Helvetica", 14))
tentativas_label.pack(pady=10)

nova_partida_button = tk.Button(janela, text="Nova Partida", command=nova_partida, font=("Helvetica", 14))
nova_partida_button.pack(pady=10)

# Iniciar a primeira partida
nova_partida()

janela.mainloop()