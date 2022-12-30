'''
from random import randint
from time import sleep
cont = 0
computador = 111
jogador = 73
while computador != jogador:
    computador = randint(0,10)
    print('='*40)
    print('Estou pensando em um numero de 0 à 10 tente adivinhar!')
    print('='*40)
    sleep(0.5)
    jogador = int(input('Qual numero eu pensei? '))
    cont += 1
    print('Eu pensei em {} e você acha que é {}'.format(computador, jogador))
    sleep(1)
    print('')
print('Você acertou! você precisou de {} tentativas'.format(cont))


'''
from random import randint
from time import sleep
cont = 0
computador = 111
jogador = 73
computador = randint(0,10)
print('='*40)
print('Estou pensando em um numero de 0 à 10 tente adivinhar!')
print('='*40)
sleep(0.5)
while computador != jogador:
    jogador = int(input('Qual numero eu pensei? '))
    cont += 1
    if jogador > computador:
        print('menos... tente mais uma vez')
    elif jogador < computador:
        print('mais... tente mais uma vez')
    sleep(1)
print('Você acertou! você precisou de {} tentativas'.format(cont))

