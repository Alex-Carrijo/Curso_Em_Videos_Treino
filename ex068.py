from random import randint
from time import sleep
cont = 0
while True:
    print('~~'*20)
    n = str(input('Vamos jogar impar ou par? [S/N]: ')).upper().strip()[0]
    print('~~'*20)
    if n == 'N':
        break
    IP = str(input('IMPAR ou PAR? ')).upper().strip()[0]
    print('Então vamos nessa! ')
    sleep(0.5)
    print('Impar')
    sleep(0.5)
    print('ou')
    sleep(0.5)
    print('Par')
    computador = randint(0,10)
    pessoa = int(input('Digite o numero: '))
    soma = computador + pessoa
    PI = soma % 2
    if IP == 'P':
        if PI == 1:
            print(f'Voce perdeu o computador jogou {computador} a soma deu {soma}, que é impar')
            break
        else:
            print(f'Parabens o computador jogou {computador} a soma deu {soma}, que é par')
    elif IP == 'I':
        if PI == 0:
            print(f'Voce perdeu o computador jogou {computador} a soma deu {soma}, que é par')
            break
        else:
            print(f'Parabens o computador jogou {computador} a soma deu {soma}, que é impar')
    cont += 1
print(f'Você venceu {cont} partidas consecutivas!')
