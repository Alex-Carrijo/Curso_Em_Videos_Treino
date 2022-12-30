import random
from time import sleep
total = list()
print('--'*20)
print('JOGO DA MEGA SENA')
print('--'*20)
jogos = int(input('Digite quantos jogos você quer fazer: '))
for c in range(0, jogos):
    numeros = random.sample(range(1,61),6)
    numeros.sort()
    total.append(numeros[:])
    numeros.clear()
for c in range(0, jogos):
    print(f'O {c+1}° jogo são esses numeros {total[c]} ')
    sleep(1)
print(f'Boa Sorte!!!')