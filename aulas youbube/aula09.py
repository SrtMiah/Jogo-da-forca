# lista = [2, 6,9, 4, 0, 12, 3, 7]
# palavra = 'Lopes'

# for letra in palavra:
#     print(letra)

# for numero in range(10):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range (10):
#     print(f'{x+1} {nome}') #quando coloco "{x_1} e apos a variavel... irá aparecer a partir de 1, e nao mais de 0!"
    
# for x in range(2, 20, 2): #a partir de 2, Até o 20, de adicioonando 2!
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)