from time import sleep
soma = 0
cont = 0
for impar in range(3,500,6):
    print(impar, end = ' ')
    soma += impar
    cont += 1
print('A soma de todos os {} numeros impares multiplos de 3 é: {}'.format(cont, soma))
sleep(2)

'''for sub in range(495, 2, -6):
    soma = soma - sub
    print(sub)
print('a subtracao é: {}'.format(soma))'''