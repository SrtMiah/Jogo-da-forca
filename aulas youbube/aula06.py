n1 = n2 =0.0
media = 0.0

n1 = float(input('Digite a nota:'))
n2 = float(input('Digite outra nota:'))
#calcular a media aritmetica
media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print('Resultado: Recuperação!')
else:
    print('resultado: Reprovado!')
    
print('Sua media é {}!'.format(media))