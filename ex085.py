par = []
impar = []
total = []
for v in range(0,7):
    valor = int(input(f'Digite o {v+1}° valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    par.sort()
    impar.sort()
    total.append(par)
    total.append(impar)
print(f'Os valores pares digitados foram {total[0]}!')
print(f'Os valores impares digitados foram {total[1]}!')

'''
valores = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')
'''