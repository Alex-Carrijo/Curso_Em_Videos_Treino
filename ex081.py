lista = []

while True:
    n = int(input('Adicione um  numero: '))
    if len(lista) == 0 or n < lista[-1]:
        lista.append(n)
        print('Elemento adicionado no final da lista...')
    else:
        c = 0
        while c < len(lista):
            if n >= lista[c]:
                lista.insert(c, n)
                print(f'Elemento adicionado no posicao {c}...')
                break
            c += 1

    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Foram digitados {len(lista)} elementos!')
print(f'A lista ordenada de forma decrescente {lista}')
if 5 in lista:
    print(f'O 5 faz parte da lista!')
else:
    print(f'P elemento 5 não faz parte da lista!')
