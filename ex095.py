dados = {}
lista = []
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas foram jogadas: '))
total = 0
cont = 1
while True:
    for c in range(1, partidas+1):
        dados[f'partida{c}'] = int(input(f'Quantos gols na {c}° partida: '))
        total += dados[f'partida{c}']
    dados['total'] = total
    lista.append(dados.copy)
    dados.clear()
    r = " "
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for c in range(1,partidas+1):
    if dados[f'partida{c}'] == 1:
        print(f'=> Na {c}° partida, ele fez {dados[f"partida{c}"]} gol. ')
    if dados[f'partida{c}'] == 0:
        print(f'=> Na {c}° partida, ele não fez gol.')
    if dados[f'partida{c}'] > 1:
        print(f'=> Na {c}° partida, ele fez {dados[f"partida{c}"]} gols. ')
print(f'No total ele fez {dados["total"]} gols.')

'''
time = list()
jogador = dict()
partidas = ()
    jogador.clear()
    partidas.clear()
    jogador = ['nome'] = str(input('Nome do jogador'))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(1, tot+1):
        partidas.append(int(input(f' Quantos gols na partida {c}?'))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3'}, end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) ' ))
    if busca = 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca0}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome]};')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
        print('-'*40)
print('Volte sempre')
'''