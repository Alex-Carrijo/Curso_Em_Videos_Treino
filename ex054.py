from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo {} pessoas são maiores de idade!'.format(maior))
print('E també tivemos {} pessoas menores de idade!'.format(menor))