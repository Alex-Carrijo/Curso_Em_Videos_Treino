lista = []
c = t = 0
while True:
    n = int(input('Digite um valor: '))
    if len(lista) == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        while c < len(lista):
            if n <= lista[c]:
                lista.insert(c, n)
                print(f'Adicionado na posiçao {c}...')
                break
            c += 1

    r = str(input('Deseja encerrar [S/N]: ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input('Deseja encerrar [S/N]: ')).upper().strip()[0]
    if r == 'N':
        break
print(lista)