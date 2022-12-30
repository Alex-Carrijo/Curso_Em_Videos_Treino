from random import randint
from time import sleep
computador = randint(0, 5)
print('='*40)
print('Estou pensando em um numero de 0 à 5, tente adivinhar!')
print('='*40)
x = int(input('Em que numero eu pensei:'))
print('POCESSANDO...')
sleep(3)
if computador == x:
    print('Voce acertou o numero pensado foi: {}'.format(x))
else:
    print('Voce errou o numero pensado foi: {} nao {}'.format(computador, x))

