import random

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

def jogar():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    print("Bem vindo ao jogo da forca!")
    print("adivinhe a palavra:")

    while True:
        print(exibir_palavra(palavra, letras_certas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
              
        letra = input("Digite uma letra: ").lower()

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
            if set(letras_certas) == set(palavra):
                print(f"Parabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            if tentativas == 0:
                print(f"Game over! A palavras era {palavra}")
                break

    reiniciar = input("Deseja jovar novamente? (S/N)").lower()
    if reiniciar == 's':
       jogar()
    else:
        print("Obrigada por jogar!")

if __name__ == "__main__":
    jogar()