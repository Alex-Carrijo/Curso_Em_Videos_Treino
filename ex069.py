mas = fem = maior = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo? [F/M] ')).upper().strip()[0]
    idade = int(input('Qual é a idade? '))
    if idade > 18:
        maior += 1
    if sexo == 'M':
        mas += 1
    if sexo =='F':
        if idade < 20:
            fem +=1
    print('~~'*20)
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('~~'*20)
    if continuar == 'N':
        break
print(f'Tem {maior} pessoas maior de idade! ')
print(f'Tem {mas} homens!')
print(f'Tem {fem} mulheres menores de 20 anos!')