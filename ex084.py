pessoa = []
lista = []
maior = menor = 0
while True:
    pessoa.append(str(input('nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
#print(f'Os dados cadastrados foram {lista}')
#total = len(lista)
print(f'Você cadastrou {len(lista)} pessoas!')
print(f'O maior peso foi de {maior}Kg. Peso de', end='')
for p in lista:
    if p[1] == maior:
        print(f',  {p[0]}', end='')
print(f'O menor peso foi de {menor}Kg. Peso de', end='')
for p in lista:
    if p[1] == menor:
        print(f', {p[0]}', end='')