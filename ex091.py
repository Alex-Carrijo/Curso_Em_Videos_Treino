from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = dict()
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1,6)
    print(f'o jogado {c} jogou {jogo[f"jogador{c}"]} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)#copiado do video
for i, v in enumerate(ranking):
    print(f'O {v[0]} ficou em {i+1}° lugar com: {v[1]}')
