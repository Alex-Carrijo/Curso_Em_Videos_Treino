stop = 'S'
soma = media = cont = 0
while stop in 'Ss':
    #stop = int(input("PARAR [1] "))
    print('~~'*10)
    flag = float(input('Digite um valor: '))
    stop = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    if cont == 0:
        menor = maior = flag
    else:
        if menor > flag:
            menor = flag
        if maior < flag:
            maior = flag
    soma += flag
    cont += 1
    media = soma / cont
print('O menor valor digitado foi {}, o maior foi {} e a media foi {:.2f}, voce digitou {} numeros '.format(menor, maior, media, cont))