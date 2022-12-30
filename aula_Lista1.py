num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
for c in range(4,12):
    print(c)

#num.pop()
num.remove(2)#elemina só o primeiro elemento 2, valores não esta na lista da erro
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(3)

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}...')

a = [2,3,7,4]
#b = a # lista a igual a lista b
b = a[:]#copia da lista a
b[2] = 8 # por elas serem iguais ao alterar uma a outra tbm será alterada
print(f'Lista A: {a}')
print(f'Lista B: {b}')
