soma = 0
cont = 0
for c in range(0,6):
    if c < 1:
        s = int(input('Digite um valor: '))
    else:
        s = int(input('Digite outro valor: '))
    if s%2 == 0:
        soma += s
        cont += 1
print('Você digitou {} numeros pares e a soma deles é: {}'. format(cont,soma))