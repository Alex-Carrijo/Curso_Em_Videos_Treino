from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Suas opçoes são 
[0] Pedra
[1] Papel
[2] Tesoura ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-='*12)
print('O computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if pc == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('GANHOU')
    else:
        print('PERDEU')
elif pc == 1:
    if jogador == 0:
        print('PERDEU')
    elif jogador == 1:
        print('EMPATOU')
    else:
        print('GANHOU')
elif pc == 2:
    if jogador == 0:
        print('GANHOU')
    elif jogador == 1:
        print('PERDEU')
    else:
        print('EMPATOU')