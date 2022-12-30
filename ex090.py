situacao = {}
situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input(f'Media de {situacao["nome"]}: '))
print()
print(f'Nome: {situacao["nome"]}')
print(f'Media: {situacao["media"]}')
if situacao['media'] >= 7:
    situacao['situaçao'] = 'Aprovado'
    print('Situação é igual a aprovado!')
elif 5<= situacao['media'] < 7:
    situacao['situaçao'] = 'recuperaçao'
    print('Situação é igual a recuperacao')
else:
    situacao['situaçao'] = 'reprovado'
    print('Situação é igual a reprovado!')

''' 
for k,v in situacao.items():
    print(f'{k} tem o valor{v}')
'''