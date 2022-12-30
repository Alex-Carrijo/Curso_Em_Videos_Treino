maior = 0
menor = 0
for c in range(1,6):
    peso = int(input('Qual e o peso da {}º pessoa? '.format(c)))
    if c == 1:
        menor, menor = peso, peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {} e o maior é {}'.format(menor, maior))