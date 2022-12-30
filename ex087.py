lista = []
matriz = []
total =  c3 = l2 = 0
c = l = 1
while True:
    valor = int(input(f'Digite o numero da posição [{l}, {c}]: '))
    total += valor
    c += 1
    lista.append(valor)
    if len(lista) == 3:
        matriz.append(lista[:])
        lista.clear()
        l += 1
        c = 1
    if len(matriz) == 3:
        break
    if len(lista) == 2:
        l2 = lista[0]
for p in matriz:
    print(f'[{p[0]}]  [{p[1]}]  [{p[2]}]')
    c3 += p[2]
    if l2 < p[1]:
        l2 = p[1]
print(f'A soma de todos os numeros da matriz é: {total}')
print(f'A soma dos elementos da terceira coluna é: {c3}')
print(f'O maior valor da segunda linha é: {l2}')