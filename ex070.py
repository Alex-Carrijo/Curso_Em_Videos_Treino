total = cont = caro = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    total += preco
    if cont < 1:
        barato = nome
        menor = preco
    if menor > preco:
        menor = preco
        barato = nome
    if preco > 1000:
        caro += 1
    print('~~'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('~~'*20)
    cont += 1
    if continuar == 'N':
        break
print(f'O total gasto foi R${total}')
print(f'Foram {caro} produtos com valor maior que R$1000')
print(f'O produto mais barato foi {barato} e o preco foi R${menor}')