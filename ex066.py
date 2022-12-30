cont = soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    cont += 1
    print('Para terminar o programa digite [999]')
print(f'A quantidade de numeros digitados foi {cont} e a soma deles é {soma}')