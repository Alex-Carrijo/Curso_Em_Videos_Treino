dados = {}
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas foram jogadas: '))
total = 0
cont = 1
for c in range(1, partidas+1):
    dados[f'partida{c}'] = int(input(f'Quantos gols na {c}° partida: '))
    total += dados[f'partida{c}']
dados['total'] = total
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
jogador = dict()
partidas = ()
jogador = ['nome'] = str(input('Nome do jogador'))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(1, tot+1):
    partidas.append(int(input(f' Quantos gols na partida {c}?'))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"]} partidas.')
for i, v in enumarate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''