lista = []
matriz = []
c = l = 1

while True:
    valor = int(input(f'Digite um numero para a posição:[{l}, {c}]: '))
    c += 1
    lista.append(valor)
    if len(lista) == 3:
        matriz.append(lista[:])
        lista.clear()
        c = 1
        l += 1
    if len(matriz) == 3:
        break
for p in matriz:
    print(f'[{p[0]}]  [{p[1]}]  [{p[2]}]')

'''
lista = []
matriz = []
 c = 0
while True:
    valor = int(input(f'Digite o  numero: '))
    c += 1
    total += valor
    lista.append(valor)
    if len(lista) == 3:
        matriz.append(lista[:])
        lista.clear()
    if len(matriz) == 3:
        break
for p in matriz:
    print(f'[{p[0]}]  [{p[1]}]  [{p[2]}]')
'''

''' 
# video 86
matriz = [[],[],[]]
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
'''