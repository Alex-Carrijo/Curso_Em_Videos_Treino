flag = int(input('Digite um numero [999] para parar: ' ))
soma = cont = 0
while flag != 999:
    soma += flag
    cont += 1
    flag = int(input('Digite outro numero ou [999] para parar: '))
print('A soma dos numeros digitados foi {} , foram digitados {} numeros'.format(soma, cont))