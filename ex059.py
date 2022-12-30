x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
t = 0
while t != 5:
    t = int(input('''    [1] para somar
    [2] para multiplicar
    [3] para selecionar o maior 
    [4] para adicionar numeros
    [5] para sair
    selecione um: ''' ))
    print('=-='*10)
    if t == 1:
        print('A soma dos numeros é {} '.format(x+y))
    elif t == 2:
        print('A multiplicaçao é: {}'.format(x*y))
    elif t == 3:
        if x > y:
            print('O maior valor é o {}'.format(x))
        else:
            print('O maior valor é o {}'.format(y))
    elif t == 4:
        x = int(input('Digite o numero novo:'))
        y = int(input('Digite o numero novo:'))
    else:
        print('Opçao invalida tente novamente')
    print('=-='*10)

print('Programa encerrado!')

