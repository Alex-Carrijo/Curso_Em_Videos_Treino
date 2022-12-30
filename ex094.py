lista = ()
listam = []
dados = {}
media = ano = 0
cont = 1
while True:
    print('=-'*12)
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo[F/M]: ')).upper().strip()[0]
    lista.append(dados.copy())
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print(f'A lista tem {len(lista)} pessoas cadastradas. ')
for c in lista:
     ano = c['idade']
     media += ano
     cont += 1
print(f'A idade media é {media/cont:.2f}')
for c in lista:
    if c['sexo'] == 'F':

'''
pessoa = dict()
galela = list()
while True:
    pessoa.clear
    pessoa['nome´] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).uper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.').uper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Responda somente S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print(f'Ao todo temos {len(galera)} pessoas foram cadastradas.')
media = soma / len(galera)
print(f'A media de idade e de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nomes"]}', end='')
print()
print('D) Lista das pessoas com idade acima da media: ')
for p in galera:
    if p['idade'] >= media:
    print('    ')
    for k, v in p.items(): 
        print(f'{k} = {v}; ', end='')
    print()
print('<<< ENCERRADO >>>)
'''
