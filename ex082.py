lista = []
par = []
impar = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if (n % 2) == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'NS':
        r = str(input('Deseja continuar [N/S]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'A lista principal e {lista}')
print(f'A lista formada pelos elementos pares é {par}')
print(f'A lista formada pelos elementos impares é {impar}')