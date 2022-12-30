x = []
for c in range(0,5):
    x.append(int(input("Digite um numero: ")))
print(x)
t = 0

maior = menor = x[t]
for c,v in enumerate(x):
    if maior < x[t]:
        maior = x[t]
    if menor > x[t]:
        menor = x[t]
    t += 1

print(f'O maior valor é {maior} e está na posição',end='')
for i, v in enumerate(x):
    if v == maior:
        print(f' {i}...',end='')
print()
print(f'O menor valor é {menor} e está na posição',end='')
for i, v in enumerate(x):
    if v == menor:
        print(f' {i}...', end='')
